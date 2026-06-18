/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_woocommerce_tax_rate_locations`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_woocommerce_tax_rate_locations`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_woocommerce_tax_rate_locations` ( `location_id` bigint unsigned NOT NULL AUTO_INCREMENT, `location_code` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `tax_rate_id` bigint unsigned NOT NULL, `location_type` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, PRIMARY KEY (`location_id`), KEY `tax_rate_id` (`tax_rate_id`), KEY `location_type_code` (`location_type`(10),`location_code`(20))) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
