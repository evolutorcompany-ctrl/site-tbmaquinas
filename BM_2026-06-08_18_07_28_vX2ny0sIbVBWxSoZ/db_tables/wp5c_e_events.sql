/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_e_events`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_e_events`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_e_events` ( `id` bigint unsigned NOT NULL AUTO_INCREMENT, `event_data` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci, `created_at` datetime NOT NULL, PRIMARY KEY (`id`), KEY `created_at_index` (`created_at`)) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp5c_e_events` (`id`, `event_data`, `created_at`) VALUES (1,'{\"event\":\"modal load\",\"version\":\"\",\"details\":\"{\\\"placement\\\":\\\"Onboarding wizard\\\",\\\"step\\\":\\\"account\\\",\\\"user_state\\\":\\\"anon\\\"}\",\"ts\":\"2023-09-30T11:33:14.749+03:00\"}','2023-09-30 11:33:15');
