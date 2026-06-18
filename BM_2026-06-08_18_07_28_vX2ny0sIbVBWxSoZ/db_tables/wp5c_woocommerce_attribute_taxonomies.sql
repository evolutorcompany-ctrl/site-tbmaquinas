/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_woocommerce_attribute_taxonomies`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_woocommerce_attribute_taxonomies`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_woocommerce_attribute_taxonomies` ( `attribute_id` bigint unsigned NOT NULL AUTO_INCREMENT, `attribute_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `attribute_label` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL, `attribute_type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `attribute_orderby` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `attribute_public` int NOT NULL DEFAULT '1', PRIMARY KEY (`attribute_id`), KEY `attribute_name` (`attribute_name`(20))) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
