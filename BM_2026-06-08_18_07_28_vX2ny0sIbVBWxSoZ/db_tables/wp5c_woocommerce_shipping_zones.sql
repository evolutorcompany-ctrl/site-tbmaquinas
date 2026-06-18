/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_woocommerce_shipping_zones`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_woocommerce_shipping_zones`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_woocommerce_shipping_zones` ( `zone_id` bigint unsigned NOT NULL AUTO_INCREMENT, `zone_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `zone_order` bigint unsigned NOT NULL, PRIMARY KEY (`zone_id`), KEY `zone_order_id` (`zone_order`,`zone_id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
