/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_woocommerce_shipping_zone_locations`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_woocommerce_shipping_zone_locations`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_woocommerce_shipping_zone_locations` ( `location_id` bigint unsigned NOT NULL AUTO_INCREMENT, `zone_id` bigint unsigned NOT NULL, `location_code` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `location_type` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, PRIMARY KEY (`location_id`), KEY `location_id` (`location_id`), KEY `location_type_code` (`location_type`(10),`location_code`(20)), KEY `zone_id` (`zone_id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
