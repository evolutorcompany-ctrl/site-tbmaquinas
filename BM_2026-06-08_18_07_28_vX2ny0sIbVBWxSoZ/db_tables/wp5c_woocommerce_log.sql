/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_woocommerce_log`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_woocommerce_log`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_woocommerce_log` ( `log_id` bigint unsigned NOT NULL AUTO_INCREMENT, `timestamp` datetime NOT NULL, `level` smallint NOT NULL, `source` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `context` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci, PRIMARY KEY (`log_id`), KEY `level` (`level`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
