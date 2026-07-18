# Discord Datamining Weekly Report - 2026-07-18

- 처리 기간: `2026-07-15T04:01:18Z` - `2026-07-18T04:06:34Z`
- 실행 시각: `2026-07-18 13:06:34 KST`
- build_hash: `2949f1429e4e8f80aaf4a349ffdd961a60a52fe4`
- 근거 번들: `canary/web.4d92efe5baf0642e.js`
- 입력 기준: `data/history.json`을 우선 확인하고 현재 추출 history 및 tracked `data/web/*`와 대조했습니다. local history에서 빠진 실험 8개와 문자열 36개를 복구했으며, `latest_changes.json`의 빈 배열은 보조 신호로만 사용했습니다.

## 핵심 요약

- 이번 창의 실험 row는 14개입니다. 실제 화면 소비가 확인된 3개를 새로 해석하고, 기존 해석 2개를 현재 설정과 소비 범위에 맞게 다시 확인했습니다.
- Clips에서는 게임 활동 패널의 저장 버튼과 클립 재생 막대의 처치·연속 처치·사망 표시가 각각 확인됐습니다. 퀘스트 바 후원 퀘스트 후보는 기본 10분과 빠른 30초 재확인 주기를 비교합니다.
- 사용자 화면 가능성은 있지만 연결 근거가 부족한 4개는 unresolved로 남겼습니다. 브라우저 성능 수집과 이미지 요청 크기 최적화 2개는 내부/저가치로 분류했습니다.
- 실험 외에는 게임 서버 호스팅 Shop, 프로필 이미지 자르기 접근성, Nitro 프로필 미리보기, 친구 장식에서 Shop으로 이어지는 문구, Family Center 보호자 연결 문구 정리가 주요 변화입니다.

## 실험 전수 분석 결과

### interpreted

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-06-clips-secondary-entrypoints | 2026-07-15T20:53:17Z | added | the game activity panel reads enableGamePanelEntrypoint and renders a save-clip button | ClipsPanelButton checks Clips availability, attached source state, and starts a clip save on click. |
| 2026-07-ad-recheck-interval-experiment | 2026-07-16T16:05:50Z | added | the Quest-bar candidate hook reads the flag and changes its recheck interval from ten minutes to thirty seconds | useQuestForAdPlacement consumes enableFastAdRecheck with focus, cache, and request guards. |
| 2026-07-clips-game-events-on-player | 2026-07-17T23:31:12.741080+00:00 | added | the Clips player reads the flag and renders kill, multikill, and death indicators on the playback bar | useClipTimelineIndicators and clip timeline serialization consume the flag; matching strings were added. |

### strengthened_existing

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-04-consistent-profiles | 2026-07-15T17:24:14.017165+00:00 | modified | current member-list consumer reconfirms the existing interpretation; the new second treatment label does not establish a mutual-friends nameplate surface | PeopleUserInfo still reads enabled; showMutualFriendsNameplate has no current UI consumer. |
| 2026-06-ml-offer-creation-ui-upgrade | 2026-07-17T16:21:52.187492+00:00 | modified | the current Nitro tab consumer reconfirms badge style and explanation surface; raw default and variation values are unchanged | NitroTabButton still reads badgeStyle and surface. |

### unresolved_needs_evidence

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-07-bounties-vertical-scroll | 2026-07-15T17:51:39Z | added | rich vertical-scroll and affordance settings are registered, but the registration result is not assigned or read | Quest module registration found; no useConfig/getConfig or exported helper consumer found. |
| 2026-07-collectibles-promotion-endpoint-reference | 2026-07-15T23:56:50Z | added | no raw settings, exact experiment match, endpoint consumer, or Shop component linkage was found | The nearby Offer Eligible string is insufficient to tie a visible promotion flow to this experiment. |
| 2026-06-wysiwyg-user-profile-premium-try-it-out | 2026-07-17T05:29:05Z | added | Nitro profile-preview strings exist, but no exact experiment match or config consumer links them to this experiment | Surprise Me and profile-with-Nitro preview copy confirm a feature surface, not the experiment linkage. |
| 2026-03-boost-to-unlock-mobile-coachmark | 2026-07-17T18:39:48.052938+00:00 | added | the flag gates mobile powerup data fetching, but no visible coachmark component reads it directly | GuildPowerupsManager consumes showCoachmark only in the fetch prerequisite path. |

### internal_or_low_value

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-06-web-vitals-monitoring | 2026-07-15T19:17:21Z | added | the consumer samples browser performance metrics and sends diagnostics without changing a user-facing surface | init_web_vitals reads enabled/sampleRate and records startup performance metrics. |
| 2026-07-attachment-image-ladder | 2026-07-15T20:26:02Z | added | the image loader rounds requested attachment dimensions to shared size steps, an internal delivery optimization with no confirmed visible difference | ImageLoaderUtils.getSrcWithWidthAndHeight reads the flag and selects ladder dimensions. |

### deletion_only_no_context

| id | timestamp | status | reason | evidence_notes |
| --- | --- | --- | --- | --- |
| 2026-06-wishlist-pdp-gift-button-priority | 2026-07-17T18:07:01Z | deleted | deleted with no prior evidence-backed interpretation or current experiment consumer | Removed from unresolved; deletion does not establish rollout or rollback. |
| 2026-02-expiring-powerup-coachmark | 2026-07-17T18:39:48.052938+00:00 | deleted | deleted with no prior evidence-backed interpretation or current consumer to preserve | No public analysis written. |
| 2026-02-boost-to-unlock-coachmark | 2026-07-17T18:39:48.052938+00:00 | deleted | deleted with no prior evidence-backed interpretation or current consumer to preserve | No public analysis written. |

## 중요한 실험 상세 해석

### 게임 활동 패널에서 클립 저장

- id: `2026-06-clips-secondary-entrypoints`
- 요약: 게임 활동 패널에 클립 저장 버튼을 추가해, 플레이 중인 장면을 그 자리에서 클립으로 남길 수 있게 하는 실험입니다.
- 근거: 게임 활동 패널이 설정을 읽고 Clips 사용 가능 여부와 영상 소스 연결 상태에 따라 저장 버튼을 표시합니다.
- source_context: ClipsPanelButton, enableGamePanelEntrypoint, Clips Actions

### 퀘스트 바 후보 빠른 재확인

- id: `2026-07-ad-recheck-interval-experiment`
- 요약: Discord 창이 활성 상태일 때 퀘스트 바의 후원 퀘스트 후보를 더 자주 다시 확인하는 실험입니다.
- 근거: 기본 10분과 빠른 30초 주기가 코드에 명시되어 있고, 창 포커스와 후보 유효 시간 조건도 함께 적용됩니다.
- source_context: useQuestForAdPlacement, enableFastAdRecheck, Quest bar

### Clips 재생 막대 게임 이벤트

- id: `2026-07-clips-game-events-on-player`
- 요약: 저장된 클립의 재생 막대에 처치·연속 처치·사망 시점을 표시하는 실험입니다.
- 근거: 클립 재생 화면이 설정을 읽어 이벤트 표시와 Kill, Multikill, Death 설명을 렌더링합니다.
- source_context: useClipTimelineIndicators, clip_events_timeline, Kill / Multikill / Death

### 멤버 목록 프로필 해석 재확인

- id: `2026-04-consistent-profiles`
- 요약: 멤버 목록의 길드 태그와 아바타 장식 해석은 유지하되, 두 번째 비교안의 상호 친구 명판 효과는 소비 근거가 없어 보류했습니다.
- 근거: 현재 PeopleUserInfo는 enabled만 읽고 showMutualFriendsNameplate 소비 위치는 확인되지 않습니다.
- source_context: PeopleUserInfo, enabled, showMutualFriendsNameplate

### Nitro 맞춤 혜택 표시 재확인

- id: `2026-06-ml-offer-creation-ui-upgrade`
- 요약: Nitro 탭의 맞춤 혜택 배지 모양과 안내 방식을 바꾸는 기존 해석을 현재 소비 코드로 다시 확인했습니다.
- 근거: 이번 수정 row의 설정값은 이전과 같고 NitroTabButton이 badgeStyle과 surface를 계속 읽습니다.
- source_context: NitroTabButton, badgeStyle, surface

## 실험에서 나타나지 않는 변화

| area | summary | evidence_notes | confidence |
| --- | --- | --- | --- |
| 게임 서버 호스팅 Shop | Shop에서 게임을 골라 친구용 서버를 만들고, 호스팅 요금제와 Nitro 할인을 확인하는 흐름이 문자열로 드러났습니다. | Strings add Game server hosting, View Plans, subscriptions, Nitro discounts, modpack installer, backups, uptime, and DDoS protection. | high |
| 프로필 이미지 자르기 접근성 | 프로필 이미지 편집기에 가로·세로 자르기 위치, 키보드 이동, 확대 후 재배치 안내가 추가됐습니다. | Seven English strings describe the image editor, crop coordinates, arrow-key movement, and zoom prerequisite. | high |
| Nitro 프로필 미리보기 | Nitro를 적용했을 때의 프로필 모습을 미리 보고 임의 조합을 골라 보는 ‘Surprise Me!’ 흐름이 추가됐습니다. | Paired strings add Surprise Me and You're previewing what your profile could look like with Nitro. | high |
| 친구 프로필 장식에서 Shop 연결 | 친구가 사용 중인 프로필 장식을 살펴보고 마음에 드는 장식을 Shop에서 찾는 안내 문구가 추가·조정됐습니다. | Strings evolve from Check it out to friend-decoration discovery and Shop this look copy; the experiment linkage remains unconfirmed. | high |
| Family Center 보호자 연결 문구 정리 | 계정 접근 유지 중심의 기존 보호자 연결 문구가 삭제되고, 보호자가 Family Center에서 활동을 볼 수 있다는 설명 중심으로 바뀌었습니다. | English and Korean rows remove the keep-access headline and QR sharing copy while revising the connection explanation. | high |
| 스레드 음성 참여 제한 | 스레드에서 음성 통화에 참여할 권한이 없거나 참여할 수 없을 때 보여 주는 안내가 추가됐습니다. | Two English strings distinguish missing permission from a general inability to join voice in a thread. | high |
| 메시지 요청 알림 | 새 메시지 요청을 받았을 때 탭하여 검토하라는 알림 문구가 추가됐습니다. | The string Sent you a message request. Tap to review. was added with sender/count presentation copy. | high |
| 프로필 장식 동적 애니메이션 | 프로필을 열 때마다 여러 애니메이션 중 하나를 무작위로 보여 주는 ‘Dynamic’ 장식 설명이 추가되고 여러 차례 다듬어졌습니다. | Strings add Dynamic and repeatedly refine the random-animation-per-visit explanation. | high |
| 반복 구독 결제 동의 | 구매 버튼을 누르면 반복 구독이 시작되고 체험 또는 할인 뒤 정가가 청구된다는 결제 동의 문구가 더 구체적으로 바뀌었습니다. | The recurring-subscription confirmation string now spells out today's charge and the post-trial or post-discount amount. | high |
| 한국어 Shop·나이 인증·서버 찾기 보강 | 한국어 문자열에는 Shop 초안 예약, 나이 인증 방법, 서버 찾기 활동 기준, 서버 태그 잠금 해제 등 여러 기존 흐름의 안내가 대규모로 보강됐습니다. | Korean rows add or revise Store draft scheduling, video-selfie and ID verification, Discovery compliance, server-tag unlock, and navigation copy. | medium |

## Unresolved 후보와 다음 확인 포인트

- 현재 unresolved 후보는 29개입니다. 이번 창에서 삭제된 `2026-06-wishlist-pdp-gift-button-priority`는 더 이상 현재 기능 근거를 찾을 후보가 아니므로 unresolved에서 제거하고 `deletion_only_no_context`로 확정했습니다.
- 나머지 carry-forward 후보는 현재 Canary 번들, API, 영문·한국어 문자열 창을 먼저 재검색했습니다. 새 문자열이 보강된 Clips 편집기·Shop this look·wishlist 계열도 실험 연결 소비가 없어 해석을 붙이지 않았습니다.

| id | timestamp | status | reason | next_check_hint |
| --- | --- | --- | --- | --- |
| 2026-05-dvp-for-attachments | 2026-06-12T20:47:43Z | needs_evidence | no current experiment id or config consumer; attachment/viewer strings are still not enough to link the feature | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-remove-wishlist-dm-sidebar-side-copy | 2026-06-10T15:05:19Z | needs_evidence | no current experiment id, config consumer, or wishlist DM-sidebar copy surface found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-bounty-use-video-modal-mobile-placement-experiment | 2026-06-13T03:48:57Z | needs_evidence | the definition remains unassigned near Quest/Bounties code and no mobile video-modal placement consumer was found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-05-bounties-stage-1 | 2026-06-13T03:48:57Z | needs_evidence | the definition remains unassigned near Quest/Bounties code; timer, Orbs amount, scrolling, and looping keys still have no confirmed config consumer | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-quest-home-layout-visual-tweaks | 2026-07-07T23:29:41.973954+00:00 | needs_config_consumer | the definition and exported helper remain, but no current visible layout read was confirmed | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-server-setup-boost-cta | 2026-06-15T22:06:33Z | needs_evidence | server perk and Boost copy exists, but no current experiment id or config consumer links server setup to a Boost CTA | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-non-friend-messages-requests-in-uk | 2026-06-18T18:30:11Z | needs_evidence | no current experiment id or consumer ties UK users to a changed non-friend message-request path | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-clips-editor-v2 | 2026-06-22T21:21:29Z | needs_evidence | new crop-position and image-editor strings confirm an editor surface, but no current experiment id or config consumer ties that surface to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-mobile-server-tag | 2026-06-23T05:14:29Z | needs_evidence | the current bundle still registers the experiment near server-tag state, but the result is not assigned or read by a visible mobile surface | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-polls-click-to-profile | 2026-06-26T19:09:12Z | needs_evidence | no current experiment id match or poll-click profile consumer found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-game-invites-channel | 2026-06-26T21:06:12Z | needs_evidence | a new LFG Channels help string exists, but no current experiment id or config consumer links it to this guild experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-similar-games-desktop | 2026-06-26T22:39:05Z | needs_evidence | no current experiment id match or similar-games desktop UI/API consumer found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-similar-games-mobile | 2026-06-26T22:39:05Z | needs_evidence | no current experiment id match or similar-games mobile UI/API consumer found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-server-boost-bar-nudge | 2026-06-30T19:02:56Z | needs_evidence | server perk and Boost copy exists, but no current experiment id or config consumer links the Boost bar nudge to a visible surface | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-improved-shop-loading | 2026-06-30T20:47:50Z | needs_evidence | no current experiment id or Shop loading consumer found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-05-clips-timeline | 2026-06-30T18:26:23.440905+00:00 | needs_evidence | no current experiment id or Clips timeline consumer found in the current bundle | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-orb-redemptions-billing-history | 2026-06-30T01:03:49Z | needs_evidence | new Orbs price strings exist, but no current experiment id or config consumer ties billing-history behavior to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-06-game-profile-share-link | 2026-07-01T02:02:49.926027+00:00 | needs_ui_consumer | the current consumer still confirms coded-link analytics only; showSmallEmbed has no user-visible consumer | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-07-server-tag-game-profiles-desktop | 2026-07-06T17:01:20Z | needs_evidence | server-tag and game-profile copy exists, but no current experiment id or config consumer links this desktop game profile surface to the experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| 2026-07-activity-entrypoint-ui | 2026-07-09T15:00:53Z | needs_evidence | the experiment row was added after the prior activity-panel experiment deletion, but no current exact id match or config consumer was found in the Canary bundle | Look for an exact id match or a consumer tied to the activity panel entrypoint before writing public analysis. |
| 2026-07-smag-wishlist-recommendations-dismiss-threshold | 2026-07-09T22:37:43Z | needs_evidence | wishlist recommendation wording remains present, but this experiment id has no current exact match or dismissal-threshold consumer | Recheck wishlist recommendation modules for a dismissal counter or threshold config consumer. |
| 2026-07-smag-wishlist-nitro-first-slot | 2026-07-10T00:43:48Z | needs_evidence | wishlist recommendation wording remains present, but no current exact id match or Nitro-first-slot placement consumer was confirmed | Search current wishlist recommendation rendering for a Nitro-first-slot config read or visible placement consumer. |
| 2026-07-smag-dm-sidebar-nitro-recommendation | 2026-07-10T16:35:32Z | needs_evidence | wishlist recommendation wording remains present, but the experiment id is absent and no DM-sidebar Nitro recommendation consumer was confirmed | Look for a DM sidebar recommendation component that reads this experiment or a matching config export. |
| 2026-07-shop-this-look | 2026-07-10T17:43:08Z | needs_evidence | friend-decoration and Shop this look copy is now stronger, but the experiment id is still absent and no config consumer links the visible surface to this experiment | Re-search Shop/Collectibles chunks for a consumer that ties the string to the experiment before adding analysis. |
| 2026-07-quest-bar-secondary-cta | 2026-07-10T22:13:34Z | needs_evidence | the definition remains with showPlayInstantlyLabel, but no exported-symbol or component consumer was found | Find a Quest bar component that reads the exported experiment before writing user-facing analysis. |
| 2026-07-bounties-vertical-scroll | 2026-07-15T17:51:39Z | needs_config_consumer | vertical-scroll, affordance, auto-scroll, and peek settings are registered, but the registration result is not assigned or read | Find a Quest or Bounties component that reads the experiment result before writing public analysis. |
| 2026-07-collectibles-promotion-endpoint-reference | 2026-07-15T23:56:50Z | needs_experiment_linkage | the row has no raw settings and no exact experiment, endpoint, or Shop component consumer; the nearby Offer Eligible string is not enough to link a promotion flow | Recheck Collectibles promotion-fetch code for this exact id or a returned offer object tied to a visible Shop surface. |
| 2026-06-wysiwyg-user-profile-premium-try-it-out | 2026-07-17T05:29:05Z | needs_experiment_linkage | Nitro profile-preview and Surprise Me strings confirm a visible try-it-out flow, but no exact experiment id or config consumer links that flow to this row | Find the WYSIWYG profile preview component and confirm that it reads this experiment before writing public analysis. |
| 2026-03-boost-to-unlock-mobile-coachmark | 2026-07-17T18:39:48.052938+00:00 | needs_ui_consumer | GuildPowerupsManager reads showCoachmark only to decide whether mobile powerup data should be fetched; no visible coachmark component reads the setting directly | Trace the mobile Boost coachmark component and confirm that the fetched powerup state plus this experiment controls its visibility. |

## 검증 및 커밋/푸시 결과

- JSON 유효성: passed
- report 구조: passed
- forbidden fallback phrase 검색: passed
- public content 검사: passed
- report pointer 일치: passed
- git diff --check: passed
- commit/push: passed (`d5c34e40b3` pushed to `origin/main`; metadata recorded by follow-up commit)
