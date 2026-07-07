# Discord String Context Report - 2026-07-07

- Generated at: 2026-07-07T09:08:14.994374Z
- Period: 2026-07-06T15:44:45Z to 2026-07-07T07:39:26.283071+00:00
- Build hash: `5cd3523a87a05ad155db18eede0a8fa55b830e66`
- Scope: cutoff 이후 history string rows에서 검색 의도가 강한 added/modified 묶음을 우선 처리하고, 최신 Family Center payload에는 `string_context`를 추가했습니다.
- Result: 6 clusters, 46 string entries annotated, 4 deferred candidates.
- Search signals: Search Console was not used. Public Google results were not required because local history/public data and current bundle snippets were sufficient.
- Source note: public `data/history.json` was absent at start; a local history snapshot was restored as an ignored validation copy.

## Clusters

|Cluster|Intent type|Confidence|Keys|Summary|
|---|---|---:|---|---|
|living-room-voice-surface|feature_or_setting_explanation|medium|DYoT0n, zQkVWf, wRLmM0, iXldTS, f7g0DK, Vm2OFQ|`Living Room`은 일반 텍스트가 아니라 Discord의 음성 채널 주변에서 보이는 별도 대화/좌석형 표면의 이름으로 보입니다.|
|storefront-preview-status|feature_or_setting_explanation|medium|c2I5Ti, eF1VJh, dX2mQt, WOZod0, QsHYzr, Id33AH, 3x/M9Z|이 문구들은 Discord 상점 또는 게임 상점 storefront가 초안, 라이브, 예약 공개, 교체됨 같은 게시 상태를 갖는 흐름을 설명합니다.|
|game-squad-linking-tags|feature_or_setting_explanation|medium|yoIAe/, vznMVa, UHF2Zn, XZapWG|이 문구들은 게임 관련 squad/post 흐름에서 Discord 계정 연결, 빈 자리 표시, 참가 요청, 태그 수 제한을 설명합니다.|
|guild-activity-summary-labels|empty_state_or_navigation|low|3Pm7uY, UoFb3H, 0CRdJQ|이 문구들은 서버별 새 항목, 멘션, 활동을 묶어 보여주는 요약 라벨로 보입니다.|
|recent-conversations-message-loading|empty_state_or_navigation|medium|aBNTxl, T3WBRp, eylmYW, u54FxB, LJuFRG|이 문구들은 최근 대화 목록을 보거나 대화가 있던 채널로 이동하는 탐색/검색형 UI에 쓰이는 라벨입니다.|
|family-center-guardian-required-disconnect|account_or_safety_notice|high|hOEHFn, Or6hgl, F2lccv, WH+Gba, o0JXuK, sCbKs4, 0ki7+P, eiABQz, PGQBnk, XyRW4c, PlrZal|이 문구들은 일부 지역의 13~16세 청소년 계정에 연결된 보호자가 필요하며, 보호자 연결을 끊으면 Discord 접근이나 Family Center 활동 정보 접근에 영향이 있음을 알립니다.|

## Annotated Strings

|Key|Lang|Status|Cluster|Value|
|---|---|---|---|---|
|DYoT0n|en|added|living-room-voice-surface|Go to Living Room|
|Vm2OFQ|en|added|living-room-voice-surface|Available Seat|
|f7g0DK|en|added|living-room-voice-surface|Back to Living Room|
|iXldTS|en|added|living-room-voice-surface|Switch back to Voice Channel|
|wRLmM0|en|added|living-room-voice-surface|Living Room|
|zQkVWf|en|added|living-room-voice-surface|Switch to Living Room|
|3x/M9Z|en|added|storefront-preview-status|This storefront was published {timestamp} and has been replaced by a newer one.|
|Id33AH|en|added|storefront-preview-status|This storefront has no scheduled publish time.|
|QsHYzr|en|added|storefront-preview-status|This storefront is live — published {timestamp}.|
|WOZod0|en|added|storefront-preview-status|This storefront goes live {timestamp}.|
|c2I5Ti|en|added|storefront-preview-status|Preview a storefront|
|dX2mQt|en|added|storefront-preview-status|{title} · Draft|
|eF1VJh|en|added|storefront-preview-status|{title} · Live|
|3x/M9Z|en|added|storefront-preview-status|This storefront was published {timestamp} and has been replaced by a newer one.|
|Id33AH|en|added|storefront-preview-status|This storefront has no scheduled publish time.|
|QsHYzr|en|added|storefront-preview-status|This storefront is live — published {timestamp}.|
|WOZod0|en|added|storefront-preview-status|This storefront goes live {timestamp}.|
|c2I5Ti|en|added|storefront-preview-status|Preview a storefront|
|dX2mQt|en|added|storefront-preview-status|{title} · Draft|
|eF1VJh|en|added|storefront-preview-status|{title} · Live|
|UHF2Zn|en|modified|game-squad-linking-tags|Link your Discord account so players can see your squad's open spots and request to join!|
|XZapWG|en|modified|game-squad-linking-tags|[Link your Discord account]({onClick}) to show live squad info and open spots.|
|vznMVa|en|modified|game-squad-linking-tags|[Link your Discord account]({onClick}) so players can see your squad's open spots!|
|yoIAe/|en|modified|game-squad-linking-tags|Add tags to help the right players find your post. Max {tagsMax} tags.|
|0CRdJQ|en|added|guild-activity-summary-labels|Activity in {guildName}{count, plural, =0 {} other { +#}}|
|0CRdJQ|en|added|guild-activity-summary-labels|Activity in {guildName}{count, plural, =0 {} other { +#}}|
|3Pm7uY|en|added|guild-activity-summary-labels|New in {guildName}{count, plural, =0 {} other { +#}}|
|3Pm7uY|en|added|guild-activity-summary-labels|New in {guildName}{count, plural, =0 {} other { +#}}|
|UoFb3H|en|added|guild-activity-summary-labels|Mentioned in {guildName}{count, plural, =0 {} other { +#}}|
|UoFb3H|en|added|guild-activity-summary-labels|Mentioned in {guildName}{count, plural, =0 {} other { +#}}|
|LJuFRG|en|added|recent-conversations-message-loading|No conversations available.|
|T3WBRp|en|added|recent-conversations-message-loading|Recent Conversations|
|aBNTxl|en|added|recent-conversations-message-loading|View in channel|
|eylmYW|en|added|recent-conversations-message-loading|We ran into an issue loading messages.|
|u54FxB|en|added|recent-conversations-message-loading|View recent conversations|
|0ki7+P|en|added|family-center-guardian-required-disconnect|I understand that disconnecting this teen will remove my access to information about their Discord activity.|
|F2lccv|en|added|family-center-guardian-required-disconnect|This will remove {username} as your connected guardian|
|Or6hgl|en|added|family-center-guardian-required-disconnect|Laws in their region require teens ages 13–16 to have a connected guardian. Without a connected guardian, {username} won’t be able to continue accessing Discord.|
|PGQBnk|en|added|family-center-guardian-required-disconnect|I understand that Discord requires at least one guardian to be connected to this teen’s account for them to continue using Discord.|
|PlrZal|en|added|family-center-guardian-required-disconnect|Disconnecting from {username} will send them a notification that you removed them. It will also revoke your access to information about their Discord activity.|
|WH+Gba|en|added|family-center-guardian-required-disconnect|This will remove your guardian connection with this account.|
|XyRW4c|en|added|family-center-guardian-required-disconnect|Disconnecting from {username} will send them a notification that you removed them. It will also revoke their access to information about your Discord activity.|
|eiABQz|en|added|family-center-guardian-required-disconnect|I understand that Discord requires at least one guardian to be connected to my account for me to continue using Discord.|
|hOEHFn|en|added|family-center-guardian-required-disconnect|Laws in your region require teens ages 13–16 to have a connected guardian. Without a connected guardian, you won’t be able to continue accessing Discord.|
|o0JXuK|en|added|family-center-guardian-required-disconnect|Disconnect from {username}?|
|sCbKs4|en|added|family-center-guardian-required-disconnect|I understand that disconnecting this guardian will remove their access to information about my Discord activity.|

## Deferred

|Key|Lang|Reason|Value|Next check|
|---|---|---|---|---|
|XhROZk|ko|low_context_label|또는|Keep deferred unless future copy gives this connector an independent feature meaning.|
|XhROZk|en|low_context_label|or|Keep deferred unless the key is repurposed into a concrete feature label.|
|DWC99q|en|low_context_label|Enabled|Annotate only if future strings tie this key to a named public setting or feature surface.|
|mgsmfY|en|internal_or_low_public_context|This flow has been disabled via developer tools|Recheck only if the same message appears in a public user flow with a concrete action or support path.|

## Validation

Passed at 2026-07-07T09:10:05.631009Z: JSON validation for public web/latest/report files plus local `data/history.json`, current-run analysis/report forbidden phrase scan, and `git diff --check`.

## Publish

- Data/report commit: `5a5a75f`
- Push: succeeded to `origin/main` at 2026-07-07T09:11:29.339884Z
- Metadata reconciliation: this report records the pushed data commit.
