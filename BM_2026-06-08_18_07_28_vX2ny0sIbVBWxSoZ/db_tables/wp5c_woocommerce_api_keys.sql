/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_woocommerce_api_keys`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_woocommerce_api_keys`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_woocommerce_api_keys` ( `key_id` bigint unsigned NOT NULL AUTO_INCREMENT, `user_id` bigint unsigned NOT NULL, `description` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci DEFAULT NULL, `permissions` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `consumer_key` char(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `consumer_secret` char(43) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `nonces` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci, `truncated_key` char(7) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `last_access` datetime DEFAULT NULL, PRIMARY KEY (`key_id`), KEY `consumer_key` (`consumer_key`), KEY `consumer_secret` (`consumer_secret`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
