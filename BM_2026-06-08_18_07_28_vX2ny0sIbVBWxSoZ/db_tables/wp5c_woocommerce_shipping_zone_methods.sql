/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_woocommerce_shipping_zone_methods`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_woocommerce_shipping_zone_methods`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_woocommerce_shipping_zone_methods` ( `zone_id` bigint unsigned NOT NULL, `instance_id` bigint unsigned NOT NULL AUTO_INCREMENT, `method_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `method_order` bigint unsigned NOT NULL, `is_enabled` tinyint(1) NOT NULL DEFAULT '1', PRIMARY KEY (`instance_id`), KEY `zone_id` (`zone_id`), KEY `method_id` (`method_id`(20))) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
