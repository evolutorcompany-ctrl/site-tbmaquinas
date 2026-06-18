/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_wc_product_download_directories`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_wc_product_download_directories`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_wc_product_download_directories` ( `url_id` bigint unsigned NOT NULL AUTO_INCREMENT, `url` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `enabled` tinyint(1) NOT NULL DEFAULT '0', PRIMARY KEY (`url_id`), KEY `url` (`url`(191))) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp5c_wc_product_download_directories` (`url_id`, `url`, `enabled`) VALUES (1,'file:///home/umaprevia-maquinas/htdocs/maquinas.umaprevia.com.br/wp-content/uploads/woocommerce_uploads/',1),(2,'https://maquinas.umaprevia.com.br/wp-content/uploads/woocommerce_uploads/',1);
