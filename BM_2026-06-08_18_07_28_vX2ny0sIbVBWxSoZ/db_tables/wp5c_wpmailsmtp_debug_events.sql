/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_wpmailsmtp_debug_events`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_wpmailsmtp_debug_events`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_wpmailsmtp_debug_events` ( `id` int unsigned NOT NULL AUTO_INCREMENT, `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci, `initiator` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci, `event_type` tinyint unsigned NOT NULL DEFAULT '0', `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
