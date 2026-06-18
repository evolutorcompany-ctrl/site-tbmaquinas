/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp5c_wpmailsmtp_tasks_meta`; */
/* PRE_TABLE_NAME: `1780942049_wp5c_wpmailsmtp_tasks_meta`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp5c_wpmailsmtp_tasks_meta` ( `id` bigint NOT NULL AUTO_INCREMENT, `action` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci NOT NULL, `date` datetime NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
INSERT INTO `1780942049_wp5c_wpmailsmtp_tasks_meta` (`id`, `action`, `data`, `date`) VALUES (1,'wp_mail_smtp_admin_notifications_update','W10=','2023-10-24 02:47:34');
