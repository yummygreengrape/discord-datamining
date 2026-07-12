# Discord String Context Report - 2026-07-12

- Generated at: 2026-07-12T09:08:55.364783Z
- Period: 2026-07-10T16:35:32+00:00 to 2026-07-11T01:01:50+00:00
- Build hash: `eabac4edf27abcde81acf8ac28badbc1b30b4f2c`
- Scope: latest local history rows after the previous cutoff, plus recheck of prior deferred labels.
- Result: 6 clusters, 22 string entries annotated, 22 deferred candidates.
- Search signals: Search Console was not used. Public Google results were not required because local public data and reports were sufficient.
- Source note: Local history rows after the previous cutoff were used as the string window; public web metadata supplied the current build hash. latest_changes.json had empty string_changes.

## Clusters

|Cluster|Intent type|Confidence|Rows|Keys|Summary|
|---|---|---:|---:|---|---|
|plant-actions-status|feature_or_setting_explanation|low|6|aduS3B, cPQCeg, B0gnKP, IrukuA, yITFQ7, uUhyVw|이 문구들은 식물 오브젝트의 상태와 동작을 설명하는 라벨 묶음으로 보입니다.|
|wishlist-shop-discovery|feature_or_setting_explanation|low|2|yBivur, xNdRDO|이 문구들은 Shop이나 wishlist 주변에서 추천 항목이나 룩 관련 상품을 발견하게 하는 라벨로 보입니다.|
|channel-topic-navigation|empty_state_or_navigation|medium|4|UcQjDe, QeJIbA|이 문구들은 채널 안의 대화를 주제별로 찾아보거나 탐색하는 안내 문구입니다.|
|server-tag-boost-unlock|server_or_permission_notice|high|4|GcEkAP, yo0g7X, Yr1ogl, BNS5zl|이 문구들은 서버 부스트로 Server Tag나 서버 특전을 잠금 해제하고 유지하는 흐름을 설명합니다.|
|quest-orbs-progress-status|quest_or_reward_status|medium|3|cfE8Oh, opIMQ5, VcZC22|이 문구들은 Quest/Orbs 보상에서 다음 지급 시점이나 진행·잠금 해제 불가 상태를 나타내는 라벨로 보입니다.|
|premium-group-switch-cooldown|billing_or_subscription_issue|high|3|h1i+H8, YjSsdH, PX3Ogd|이 문구들은 Premium Group 특전에 참여하거나 다른 플랜 초대를 수락할 때 적용되는 구독 전환과 cooldown 안내입니다.|

## Annotated Strings

|Key|Lang|Status|Cluster|Value|
|---|---|---|---|---|
|yBivur|en|added|wishlist-shop-discovery|Wishlist & Recommendations|
|xNdRDO|en|added|wishlist-shop-discovery|Shop this Look|
|QeJIbA|en|deleted|channel-topic-navigation|Browse conversations happening in this channel.|
|UcQjDe|en|deleted|channel-topic-navigation|Navigate chat by topic|
|QeJIbA|en|added|channel-topic-navigation|Browse conversations happening in this channel.|
|UcQjDe|en|added|channel-topic-navigation|Navigate chat by topic|
|GcEkAP|en|added|server-tag-boost-unlock|Unlock a Server Tag with Boosts|
|yo0g7X|en|added|server-tag-boost-unlock|Let your members represent this server everywhere on Discord.|
|VcZC22|en|added|quest-orbs-progress-status|Cannot progress|
|opIMQ5|en|added|quest-orbs-progress-status|Cannot unlock|
|BNS5zl|ko|modified|server-tag-boost-unlock|오늘 만료되기 전에 {boostCount}개의 부스트를 추가해서 계속 활성 상태로 유지하세요.|
|PX3Ogd|ko|modified|premium-group-switch-cooldown|{cooldownMonths}개월마다 한 번만 {premiumGroupProductName}에 참가할 수 있어요.|
|YjSsdH|ko|modified|premium-group-switch-cooldown|{primaryName} 플랜에서 {premiumGroupProductName} 특전을 잠금 해제하도록 초대받았어요. 수락하면 현재 구독이 일할 계산 없이 즉시 종료돼요. {cooldownMonths}개월마다 한 번만 {premiumGroupProductName}에 가입할 수 있어요.|
|Yr1ogl|ko|modified|server-tag-boost-unlock|부스트 {boostCount}개만 더 있으면 모두가 {perkName} 특전을 잠금 해제할 수 있어요.|
|cfE8Oh|ko|modified|quest-orbs-progress-status|{days}일 후에 더 많은 Orbs가 찾아올 거예요!|
|h1i+H8|ko|modified|premium-group-switch-cooldown|{cooldownMonths}개월마다 한 번만 {premiumGroupProductName}에 참가할 수 있어요.|
|B0gnKP|en|added|plant-actions-status|Plant Actions|
|IrukuA|en|added|plant-actions-status|Live Plant|
|aduS3B|en|added|plant-actions-status|Water Plant|
|cPQCeg|en|added|plant-actions-status|Plant Vase|
|uUhyVw|en|added|plant-actions-status|Dead Plant|
|yITFQ7|en|added|plant-actions-status|Dying Plant|

## Deferred

|Key|Lang|Reason|Value|Next check|
|---|---|---|---|---|
|XhROZk|ko|low_context_label|또는|Keep deferred unless future copy gives this connector independent feature meaning.|
|XhROZk|en|low_context_label|or|Keep deferred unless the key is repurposed into a concrete feature label.|
|DWC99q|en|low_context_label|Enabled|Annotate only if future strings tie this key to a named public feature or setting.|
|DWC99q|ko|low_context_label|활성화됨|Keep deferred unless a future payload ties it to a specific setting name.|
|mgsmfY|en|internal_or_low_public_context|This flow has been disabled via developer tools|Recheck only if the same message appears in a public user flow with a concrete action or support path.|
|mgsmfY|ko|internal_or_low_public_context|개발자 도구를 통해 이 흐름이 비활성화되었어요|Do not annotate unless future context shows a public flow and concrete user action.|
|93KE7U|en|low_context_label|Duck|Recheck if future Living Room, sound, avatar, or activity copy ties Duck to a concrete interaction.|
|PHT1N2|en/ko|low_context_label|Primary / 기본|Annotate only if a future row makes the color role independently searchable.|
|9/wzjF|en/ko|low_context_label|Accent / 강조|Keep deferred unless future copy ties it to a named Server Tag customization setting.|
|xRxGFl|en|deferred_needs_more_context|Activity & Origins|Recheck with profile, activity, or onboarding consumers before annotating.|
|c2GSIl|en/ko|low_context_label|NEW / 신규|Annotate only if future strings tie this key to a specific named feature badge.|
|AVkYMx|en/ko|low_context_label|Personal / 개인용|Recheck if future adjacent copy names the Personal section or product surface.|
|uNGhdg|ko|low_context_label|싫어요|Annotate only if future copy ties Like/Dislike to a named recommendation, Shop, or safety flow.|
|7iRs51|ko|low_context_label|좋아요|Annotate only if future copy ties the label to a named recommendation, Shop, or safety flow.|
|6Ic4Ev|ko|low_context_label|더 많은 옵션|Keep deferred unless a future payload ties it to a named menu or settings surface.|
|nYvQ07|ko|translation_polish_low_search_intent|{count}개의 동영상을 전송했어요|Do not annotate unless future rows connect it to a named media-send feature or error.|
|KxO2Yl|ko|translation_polish_low_search_intent|동영상을 전송했어요|Do not annotate unless future rows add a user-facing media-send issue or feature name.|
|9PA6uj|ko|translation_polish_low_search_intent|스포일러 채널에 GIF 이미지를 보냈어요|Annotate only if future copy introduces a concrete GIF/spoiler failure or setting.|
|EPkGyE|ko|translation_polish_low_search_intent|{time} 시간동안 플레이 중|Do not annotate unless tied to a named Activity or Quest requirement.|
|8JRFyZ|ko|low_context_label|{count}개 아이템 더 보기|Keep deferred unless future rows name the list or item type.|
|0JYT98|ko|low_context_label|{count}개 음향 숨기기|Recheck if future soundboard copy ties it to a concrete soundboard interaction.|
|+sThav|ko|low_context_label|{hours}시간|Do not annotate standalone duration fragments.|

## Validation

- Status: passed
- python3 -m json.tool data/web/meta.json: passed
- python3 -m json.tool data/web/strings.ko.json: passed
- python3 -m json.tool data/web/strings.en.json: passed
- python3 -m json.tool data/latest_changes.json: passed
- python3 -m json.tool data/reports/string-context/latest.json: passed
- python3 -m json.tool data/reports/string-context/2026-07-12.json: passed
- python3 -m json.tool data/history.json: passed
- scoped forbidden private/token/SEO/overclaim scan: passed
- git diff --check: passed

## Publish

- Status: pushed
- Pushed: True
- Pushed at: 2026-07-12T09:11:51.107042Z
- Commit: `f8e5c5d4` Add string context interpretations for July 12 strings
- Notes: Report publish metadata is committed by a follow-up commit after the data/report publish commit.
