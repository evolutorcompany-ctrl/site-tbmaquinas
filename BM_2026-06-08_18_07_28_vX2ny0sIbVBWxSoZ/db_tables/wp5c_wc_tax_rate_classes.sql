/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_wc_tax_rate_classes`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_wc_tax_rate_classes`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_wc_tax_rate_classes` ( `tax_rate_class_id` bigint unsigned NOT NULL AUTO_INCREMENT, `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '', `slug` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL DEFAULT '', PRIMARY KEY (`tax_rate_class_id`), UNIQUE KEY `slug` (`slug`(191))) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp5c_wc_tax_rate_classes` (`tax_rate_class_id`, `name`, `slug`) VALUES (1,'Taxa reduzida','taxa-reduzida'),(2,'Taxa zero','taxa-zero');
