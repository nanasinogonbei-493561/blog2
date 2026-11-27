<?php
/**
 * WordPress SEO補助スニペット:
 * 1. 主要SEOプラグイン未導入時の meta description 出力
 * 2. 個別投稿ページ向け BlogPosting + BreadcrumbList JSON-LD 構造化データ出力
 * 3. 日英URL分離時の hreflang カスタムフィールド登録と <link rel="alternate"> 出力
 *
 * 配置先候補:
 * - 子テーマの functions.php
 * - Code Snippets プラグイン
 * - wp-content/mu-plugins/seo-jsonld-and-hreflang.php
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * 主要SEOプラグインまたはCocoon標準SEO機能が有効かどうかを判定する。
 */
function blog_has_active_seo_plugin(): bool {
	return defined( 'SSP_VERSION' )
		|| defined( 'WPSEO_VERSION' )
		|| defined( 'AIOSEO_VERSION' )
		|| defined( 'RANK_MATH_VERSION' )
		|| function_exists( 'is_cocoon_child' )
		|| ( defined( 'THEME_NAME' ) && 'cocoon' === strtolower( (string) THEME_NAME ) )
		|| 'cocoon-master' === get_template();
}

/**
 * 将来的な日英URL分離用カスタムフィールドを REST API 経由で更新できるよう登録する。
 */
function blog_register_hreflang_post_meta(): void {
	$keys = array( '_blog_hreflang_ja_url', '_blog_hreflang_en_url' );
	foreach ( $keys as $key ) {
		register_post_meta(
			'post',
			$key,
			array(
				'type'              => 'string',
				'single'            => true,
				'show_in_rest'      => true,
				'sanitize_callback' => 'esc_url_raw',
				'auth_callback'     => static function () {
					return current_user_can( 'edit_posts' );
				},
			)
		);
	}
}
add_action( 'init', 'blog_register_hreflang_post_meta' );

/**
 * SEOプラグイン未導入時に抜粋ベースの meta description を出力する。
 */
function blog_output_fallback_meta_description(): void {
	if ( blog_has_active_seo_plugin() || is_admin() ) {
		return;
	}

	$description = '';
	if ( is_singular( 'post' ) ) {
		$post = get_queried_object();
		if ( $post instanceof WP_Post ) {
			$raw = has_excerpt( $post ) ? $post->post_excerpt : wp_strip_all_tags( $post->post_content );
			$description = wp_html_excerpt( preg_replace( '/\s+/u', ' ', trim( $raw ) ), 160, '…' );
		}
	} elseif ( is_home() || is_front_page() ) {
		$description = get_bloginfo( 'description' );
		if ( '' === trim( (string) $description ) ) {
			$description = 'プログラミング未経験からの学習記録、日常の小さな不便を自作アプリで解決する進め方、Build in Publicの試行錯誤をまとめています。';
		}
	}

	if ( '' !== trim( (string) $description ) ) {
		echo '<meta name="description" content="' . esc_attr( $description ) . '" />' . "\n";
	}
}
add_action( 'wp_head', 'blog_output_fallback_meta_description', 1 );

/**
 * SEOプラグイン未導入時に個別投稿の JSON-LD (BlogPosting / BreadcrumbList) を出力する。
 */
function blog_output_post_jsonld(): void {
	if ( blog_has_active_seo_plugin() || ! is_singular( 'post' ) ) {
		return;
	}

	$post = get_queried_object();
	if ( ! ( $post instanceof WP_Post ) ) {
		return;
	}

	$permalink   = get_permalink( $post );
	$raw_excerpt = has_excerpt( $post ) ? $post->post_excerpt : wp_strip_all_tags( $post->post_content );
	$description = wp_html_excerpt( preg_replace( '/\s+/u', ' ', trim( $raw_excerpt ) ), 160, '…' );
	$image_url   = get_the_post_thumbnail_url( $post, 'full' );
	$author_name = get_the_author_meta( 'display_name', (int) $post->post_author );

	$blog_posting = array(
		'@context'         => 'https://schema.org',
		'@type'            => 'BlogPosting',
		'mainEntityOfPage' => array(
			'@type' => 'WebPage',
			'@id'   => $permalink,
		),
		'headline'         => get_the_title( $post ),
		'description'      => $description,
		'datePublished'    => get_the_date( DATE_W3C, $post ),
		'dateModified'     => get_the_modified_date( DATE_W3C, $post ),
		'author'           => array(
			'@type' => 'Person',
			'name'  => $author_name ?: get_bloginfo( 'name' ),
		),
		'publisher'        => array(
			'@type' => 'Organization',
			'name'  => get_bloginfo( 'name' ),
		),
	);

	if ( $image_url ) {
		$blog_posting['image'] = array( $image_url );
	}

	$breadcrumbs = array(
		array(
			'@type'    => 'ListItem',
			'position' => 1,
			'name'     => 'ホーム',
			'item'     => home_url( '/' ),
		),
	);

	$categories = get_the_category( $post->ID );
	if ( ! empty( $categories ) && ! is_wp_error( $categories ) ) {
		$primary       = $categories[0];
		$breadcrumbs[] = array(
			'@type'    => 'ListItem',
			'position' => 2,
			'name'     => $primary->name,
			'item'     => get_category_link( $primary->term_id ),
		);
		$breadcrumbs[] = array(
			'@type'    => 'ListItem',
			'position' => 3,
			'name'     => get_the_title( $post ),
			'item'     => $permalink,
		);
	} else {
		$breadcrumbs[] = array(
			'@type'    => 'ListItem',
			'position' => 2,
			'name'     => get_the_title( $post ),
			'item'     => $permalink,
		);
	}

	$breadcrumb_ld = array(
		'@context'        => 'https://schema.org',
		'@type'           => 'BreadcrumbList',
		'itemListElement' => $breadcrumbs,
	);

	$flags = JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES;
	echo '<script type="application/ld+json">' . wp_json_encode( $blog_posting, $flags ) . '</script>' . "\n";
	echo '<script type="application/ld+json">' . wp_json_encode( $breadcrumb_ld, $flags ) . '</script>' . "\n";
}
add_action( 'wp_head', 'blog_output_post_jsonld', 2 );

/**
 * 日英URLが両方設定された投稿に hreflang タグを出力する。
 */
function blog_output_hreflang_links(): void {
	if ( ! is_singular( 'post' ) ) {
		return;
	}

	$post_id = get_queried_object_id();
	if ( ! $post_id ) {
		return;
	}

	$ja_url = trim( (string) get_post_meta( $post_id, '_blog_hreflang_ja_url', true ) );
	$en_url = trim( (string) get_post_meta( $post_id, '_blog_hreflang_en_url', true ) );

	if ( '' === $ja_url || '' === $en_url ) {
		return;
	}

	echo '<link rel="alternate" hreflang="ja" href="' . esc_url( $ja_url ) . '" />' . "\n";
	echo '<link rel="alternate" hreflang="en" href="' . esc_url( $en_url ) . '" />' . "\n";
	echo '<link rel="alternate" hreflang="x-default" href="' . esc_url( $ja_url ) . '" />' . "\n";
}
add_action( 'wp_head', 'blog_output_hreflang_links', 3 );
