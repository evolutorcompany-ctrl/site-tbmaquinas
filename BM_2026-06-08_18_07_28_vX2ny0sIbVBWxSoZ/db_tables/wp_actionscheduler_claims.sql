/* CUSTOM VARS START */
/* REAL_TABLE_NAME: `wp_actionscheduler_claims`; */
/* PRE_TABLE_NAME: `1780942049_wp_actionscheduler_claims`; */
/* CUSTOM VARS END */

CREATE TABLE IF NOT EXISTS `1780942049_wp_actionscheduler_claims` ( `claim_id` bigint unsigned NOT NULL AUTO_INCREMENT, `date_created_gmt` datetime DEFAULT '0000-00-00 00:00:00', PRIMARY KEY (`claim_id`), KEY `date_created_gmt` (`date_created_gmt`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
