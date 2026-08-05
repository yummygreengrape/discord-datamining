# Discord 데이터마이닝 주간 리포트 — 2026-08-05

## 처리 기간과 빌드

- 처리 기간: `2026-08-01T04:17:31Z` ~ `2026-08-05T04:13:55Z`
- build_hash: `5c4bc184b890390dd26244becef39234ec252a8e`
- 근거 번들: `canary/web.dd10995c95a24481.js`
- 입력 기준: ignored `data/history.json`을 우선 확인하고 paired extraction history 및 tracked `data/web/*`와 대조했습니다. 빠진 실험 10행과 문자열 174행을 동기화했으며, `latest_changes.json`의 빈 change 배열은 보조 신호로만 사용했습니다.

## 핵심 요약

- 실험 10행 / 10개 ID, API 2행, 문자열 206행(201개 고유 행)을 검토했습니다.
- 새 해석은 3행, 삭제 맥락 보존은 2행, 근거 보류는 3행, 보존 맥락 없는 삭제는 2행입니다.
- Nitro 탭의 Call of Duty: MW4 보상 안내 2개와 웹 개별 파일 최소 20MB 한도 실험을 새로 해석했습니다.
- raw 갱신으로 사라진 근거 있는 해석 12행을 이전 게시본과 현재 소비 경로를 대조해 복구했습니다. 북마크·리마인더 v2와 서버 앱 제작 실험 설명도 최신 문자열에 맞춰 보강했습니다.
- 이전 unresolved 40건을 먼저 재검색했습니다. 삭제된 wishlist 문구 후보 1건을 제거하고 새 후보 3건을 더해 42건을 이월합니다.

## 실험 전수 분석 결과

### interpreted

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-07-call-of-duty-3pp-non-sub-marketing` | `2026-08-03T19:51:19Z` | added | interpreted | the Nitro tab reads the config for non-subscribers and adds a New badge, popover, signup action, and MW4 reward deep link |
| `2026-07-call-of-duty-3pp-marketing` | `2026-08-03T19:51:19Z` | added | interpreted | the Nitro tab reads the config for subscribers and adds a reward badge, popover, and MW4 reward deep link |
| `2026-08-kestrel-ga` | `2026-08-03T21:31:48.819737+00:00` | added | interpreted | web upload preflight and oversized-file errors read the config and use a minimum 20 MB per-file limit |

### strengthened / deleted context

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-05-mobile-lurker-server-preview` | `2026-08-03T14:43:48Z` | deleted | deleted_preserved_context | prior behavior-linked server-preview retention context is preserved on the deletion row |
| `2026-05-game-mentions-v2` | `2026-08-03T17:44:16Z` | deleted | deleted_preserved_context | prior behavior-linked game-mention autocomplete context is preserved on deletion |

### unresolved

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-07-game-mentions-v2-mobile` | `2026-08-03T17:44:16Z` | added | unresolved_needs_evidence | the exact registration is present but its config result is not assigned or read |
| `2026-07-personal-widget` | `2026-08-03T19:19:03Z` | added | unresolved_needs_evidence | profile-widget UI, strings, and clip upload are visible, but none is linked to the three experiment variants |
| `2026-07-clips-editor-text-track` | `2026-08-03T22:01:29Z` | added | unresolved_needs_evidence | no exact registration, config consumer, text-track editor component, or linked string was found |

### skipped / deletion-only

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-06-remove-wishlist-dm-sidebar-side-copy` | `2026-08-04T15:57:40Z` | deleted | deletion_only_no_context | the previously unresolved row was deleted without a prior evidence-backed interpretation or current consumer |
| `2026-05-expiring-boosts` | `2026-08-04T16:11:48Z` | deleted | deletion_only_no_context | deleted without a prior evidence-backed interpretation or a current exact consumer |

## 중요한 실험 상세 해석

### Nitro 구독자용 MW4 보상 안내 (`2026-07-call-of-duty-3pp-marketing`)

Nitro 탭에 보상 배지와 팝오버를 띄우고 MW4 얼리 액세스 코드 카드로 이동시킵니다.

- 근거: The subscriber marketing helper is read by NitroTabButton and adds COD_3PP_POPOVER plus a reward deep link.
- 확인 위치: COD_3PP_POPOVER, REWARD, Claim Reward, CALL_OF_DUTY_3PP_CARD_ID

### Nitro 미구독자용 MW4 가입 안내 (`2026-07-call-of-duty-3pp-non-sub-marketing`)

Nitro 탭의 새 기능 배지와 팝오버에서 Nitro 가입을 거쳐 MW4 보상 카드로 연결합니다.

- 근거: The non-subscriber helper is read by NitroTabButton and connects Get Nitro to the same reward destination.
- 확인 위치: New badge, Get Nitro, MW4 Early Access Beta, CALL_OF_DUTY_3PP_CARD_ID

### 웹 개별 파일 최소 20MB 한도 (`2026-08-kestrel-ga`)

기존 한도가 더 작을 때 웹의 개별 파일 허용 크기를 20MB로 계산하고 오류 안내도 같은 값을 사용합니다.

- 근거: Upload preflight and visible errors both read the GA config and preserve any existing limit above 20 MB.
- 확인 위치: 20 MB threshold, filesExceedUploadLimits, FILE_SIZE_LIMIT_EXCEEDED, max file size

### 북마크·리마인더 안내 보강 (`2026-07-message-bookmarks-v2`)

데스크톱·모바일 생성 방법, 빈 목록, 계정 한도와 Nitro 확장 안내를 기존 기능 설명에 반영했습니다.

- 근거: Current consumers still read the v2 config, while the new strings make creation and capacity behavior explicit.
- 확인 위치: Right-click any message, Long press any message, Bookmark limit reached, Reminder limit reached

### 앱 제작 화면 명칭 갱신 (`2026-07-vibegrations-guild`)

기존 제작·미리보기·게시 흐름은 유지하면서 사용자 표시 이름을 Projects와 Create 중심으로 바꿨습니다.

- 근거: The permission-gated consumer remains active and current strings replace Conjurings and Magic Builder terminology.
- 확인 위치: Your Projects, Create, private until you publish, Manage Channels and Manage Guild

## 실험에서 나타나지 않는 변화

| 영역 | 제품 변화 | 근거와 확신도 |
|---|---|---|
| 프로필 위젯과 게임 클립 | 프로필 위젯에 게임에서 만든 클립을 올리는 전용 업로드 경로와 진행 상태가 추가됐고, 개인 위젯을 추가하거나 Nitro로 직접 만드는 진입점도 나타났습니다. | The new widget clip-upload endpoint is consumed by the widget action, while strings add Add Clip, Uploading clip, game-only validation, Add Personal Widget, and View Widget. (high) |
| Living Room 좌석과 상태 | Living Room 화면이 좌석 수, 빈자리, 방 안의 물건 수를 안내하고 각 사용자의 자리·AFK·컨트롤러·노트북·책·담요 상태를 표시하는 문구를 갖췄습니다. | A coherent string cluster names numbered rooms, occupied seats, full or unavailable rooms, open spots, objects, and per-user seat accessories. (high) |
| 메시지 북마크·리마인더 안내 | 우클릭·길게 누르기로 북마크와 리마인더를 만드는 방법, 빈 목록, 한도 초과, Nitro에서 늘어나는 저장 수를 설명하는 안내가 대폭 보강됐습니다. | New desktop and mobile onboarding, empty-state replacements, limit errors, deletion guidance, and Nitro capacity copy align with the existing saved-message consumers. (high) |
| Call of Duty: MW4 Nitro 보상 | Nitro Home에 MW4 얼리 액세스 베타 코드의 잠금 해제·수령·등록·만료와 출시 후 청사진 보상을 안내하는 영어·한국어 흐름이 추가됐습니다. | A paired bilingual cluster covers subscriber and acquisition copy, one-time codes, valid dates, redemption, expiration, and a launch reward. (high) |
| 앱 제작 화면의 Projects·Create 표현 | 앱 제작 화면이 ‘Your Conjurings’를 ‘Your Projects’로, ‘Magic Builder’를 ‘Create’로 바꾸고 프로젝트는 게시 전까지 비공개라고 안내합니다. | Three modified strings and one deleted App label simplify the user-facing name without evidence that the underlying build and publish flow was removed. (high) |
| 프로필 꾸미기 미리보기 | 애니메이션 아바타, 배너 이미지·색상, 기본색·강조색, 표시 이름 스타일을 실제 적용 전에 시험하고 현재 값을 확인하는 문구가 추가됐습니다. | The profile customization cluster contains paired try-out and change actions plus current-value and accessibility descriptions. (high) |
| Shop 협업·혜택 필터 | 한국어 Shop 문구에 협업 항목 수, 이용 가능한 혜택 수, 혜택 사용, 아이템 받기, 직접 구매 동작이 추가되거나 자연스럽게 다듬어졌습니다. | Korean strings add Collabs and Offer Eligible counters plus redeem and claim actions, while Buy for myself becomes Buy directly. (high) |
| 웹 파일 업로드 한도 안내 | 파일이 너무 클 때 현재 최대 크기와 Nitro에서 가능한 더 큰 크기를 함께 알려 주는 문구가 추가됐습니다. | The current upload preflight and error modal share the effective per-file limit, and the new string presents both current and premium maxima. (high) |
| 채널·DM Favorites 모바일 안내 | 채널이나 DM을 길게 눌러 Favorites에 추가하고 빠르게 다시 여는 모바일 안내가 추가됐습니다. | The string explicitly names the long-press action, both channel and DM targets, and the quick-access result. (high) |
| 분리된 메시지·공유 설정 단서 | Silent message, Preparing to share, Typing Indicator라는 새 문구가 각각 나타났습니다. 현재 변경만으로 정확한 조작 위치나 기본 동작까지는 확인되지 않았습니다. | These are isolated labels rather than a connected flow, so the report records the surfaces without inferring behavior. (medium) |

## unresolved 후보와 다음 확인 포인트

| ID | 보류 이유 | 다음 확인 |
|---|---|---|
| `2026-05-dvp-for-attachments` | no current experiment id or config consumer; attachment/viewer strings are still not enough to link the feature | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-05-bounties-stage-1` | the current bundle still registers timer, Orbs, looping, and scroll settings without assigning or reading the experiment result | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-server-setup-boost-cta` | server perk and Boost copy exists, but no current experiment id or config consumer links server setup to a Boost CTA | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-non-friend-messages-requests-in-uk` | no current experiment id or consumer ties UK users to a changed non-friend message-request path | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-clips-editor-v2` | the current bundle still has no exact id or config consumer; new Clip Quality copy confirms a settings surface but does not link it to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-mobile-server-tag` | the current guild profile/store module still registers the experiment without assigning or reading the returned config | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-game-invites-channel` | new built-in-voice LFG copy confirms a product surface, but no current exact id or config consumer links it to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-similar-games-desktop` | new game-profile preference and autocomplete copy appeared, but no exact id or similar-games desktop consumer was found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-similar-games-mobile` | new game-profile preference and autocomplete copy appeared, but no exact id or similar-games mobile consumer was found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-orb-redemptions-billing-history` | partner and Orbs benefit copy changed, but no exact id or billing-history config consumer links those strings to this experiment | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-05-clips-timeline` | no current experiment id or Clips timeline consumer found in the current bundle | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-server-boost-bar-nudge` | server perk and Boost copy exists, but no current experiment id or config consumer links the Boost bar nudge to a visible surface | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-improved-shop-loading` | no current experiment id or Shop loading consumer found | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-07-server-tag-game-profiles-desktop` | a new guild-profile-server-tag row and game-profile copy appeared, but no exact id or desktop server-tag consumer was confirmed | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-06-quest-home-layout-visual-tweaks` | the current Quest module exports the experiment, but none of the current import sites reads the exported Mk object | Re-search the current Canary bundle for a concrete useConfig/getConfig consumer, route, store/action, component, or user-facing string linkage before writing public analysis. |
| `2026-07-activity-entrypoint-ui` | new activity popout and chat-control strings confirm a broader activity surface, but no exact id or activity-entrypoint config consumer was found | Look for an exact id match or a consumer tied to the activity panel entrypoint before writing public analysis. |
| `2026-07-smag-wishlist-recommendations-dismiss-threshold` | wishlist routes and a new direct-to-gifting row are present, but no exact id or dismissal-threshold consumer was found | Recheck wishlist recommendation modules for a dismissal counter or threshold config consumer. |
| `2026-07-smag-wishlist-nitro-first-slot` | wishlist routes and a new direct-to-gifting row are present, but no exact id or Nitro-first-slot consumer was found | Search current wishlist recommendation rendering for a Nitro-first-slot config read or visible placement consumer. |
| `2026-07-smag-dm-sidebar-nitro-recommendation` | wishlist routes and a new direct-to-gifting row are present, but no exact id or DM-sidebar Nitro recommendation consumer was found | Look for a DM sidebar recommendation component that reads this experiment or a matching config export. |
| `2026-07-shop-this-look` | the current bundle exposes a Shop this Look marketing dismissible-content marker and Shop copy, but no exact experiment id or config consumer links that surface to this row | Trace the Shop this Look dismissible content to an exact experiment read before adding public analysis. |
| `2026-07-quest-bar-secondary-cta` | showPlayInstantlyLabel remains defined, but the experiment is not exported to or read by a Quest bar component | Find a Quest bar component that reads the exported experiment before writing user-facing analysis. |
| `2026-07-bounties-vertical-scroll` | vertical-scroll and auto-scroll settings remain registered, but the returned experiment object is not assigned or consumed | Find a Quest or Bounties component that reads the experiment result before writing public analysis. |
| `2026-07-collectibles-promotion-endpoint-reference` | new Korean Collabs, Offer Eligible, redeem, and item-claim copy strengthens the Shop offer surface, but no exact experiment or endpoint consumer links it to this row | Trace the Shop offer-filter and redemption code to an exact experiment or endpoint reference before adding public analysis. |
| `2026-06-wysiwyg-user-profile-premium-try-it-out` | new profile try-out strings confirm animated avatar, banner, color, and display-name previews, but no exact experiment id or config consumer links the preview surface to this row | Find the profile try-out renderer and confirm that it reads this experiment before writing public analysis. |
| `2026-03-boost-to-unlock-mobile-coachmark` | GuildPowerupsManager still reads showCoachmark only to decide whether powerup data should be fetched; no visible coachmark component was confirmed | Trace the mobile Boost coachmark component and confirm that the fetched powerup state plus this experiment controls its visibility. |
| `2026-07-wishlist-direct-to-gifting` | wishlist and gifting flows exist, but no exact experiment match or variant consumer links them to this row | Find a wishlist item or gifting action that reads this experiment and distinguishes Variant 1 from Variant 2 before writing public analysis. |
| `2026-06-guild-profile-server-tag` | server-tag state and profile copy exist, but no exact experiment match or config consumer connects this row to the visible guild profile | Trace guild-profile tag rendering to an exact experiment read or matching exported helper before writing public analysis. |
| `2026-06-game-server-hosting-in-shop` | the current bundle exposes a game-server-hosting Shop banner marker, but no exact experiment id or variant consumer links the three treatments to Shop placement | Trace the Shop game-server-hosting banner to this experiment and map the variants before writing public analysis. |
| `2026-07-powerups-coachmark-scroll-close` | Powerups coachmark code exists, but no exact experiment match or scroll-close consumer links that behavior to this row | Trace the visible Powerups coachmark close handler and confirm that scrolling reads this experiment before writing public analysis. |
| `2026-07-collectibles-collabs-filter` | Collabs, Collabs counts, and Offer Eligible counts confirm a Shop filter surface, but no exact experiment id or filter consumer was found | Trace the Shop filter rendering and confirm an exact experiment read before adding public analysis. |
| `2026-05-quest-home-tile-redesign` | the current definition exports layout and clickable-tile options, but none of the current import sites reads the exported aD experiment object | Find a Quest Home tile or layout component that reads the exported experiment object before writing public analysis. |
| `2026-06-hero-shelf-ad-tile` | the row suggests a visible advertising tile, but no exact experiment id, shelf component, route, or treatment consumer was found | Find a rendered shelf or advertising card that reads this experiment before writing public analysis. |
| `2026-07-nitro-home-header-followup` | Nitro Home and free Shop-item strings changed, but no exact experiment id or header variant consumer was found | Trace the Nitro Home header component and confirm how Variant 0 and Variant 1 change the visible header. |
| `2026-07-gdop-discovery` | no exact experiment id, config consumer, route, or visible discovery component was found | Find an exact experiment registration or discovery component that distinguishes Variant 0 from Variant 1. |
| `2026-07-social-layer-storefront-spend-orbs-banner-copy` | time-limited Nitro and Orbs item copy confirms a storefront banner surface, but no exact experiment id or variant consumer links that copy to this row | Trace the social-layer storefront banner renderer to an exact experiment read and compare the two copy variants. |
| `2026-07-call-of-duty-3pp-expired` | the exact experiment is now registered beside the Call of Duty marketing configs, and expiry strings exist, but its returned config is not assigned, exported, or read by the visible reward card | Find an expired-state component that directly reads this experiment before adding public analysis. |
| `2026-07-cod-3pp` | the exact experiment now exports a config helper, but no current caller uses that base helper; only the two sibling marketing experiments are read by the Nitro tab | Find a Call of Duty provider or reward entrypoint that calls the base experiment helper before writing public analysis. |
| `2026-07-wishlist-show-owned-items-last` | wishlist and gifting surfaces exist, but no exact experiment id or owned-item sorting consumer was found | Find the wishlist item sorter and confirm that it reads this experiment before moving owned items to the end. |
| `2026-08-soundboard-desktop-nux` | the current bundle exposes a SOUNDBOARD_DESKTOP_NUX dismissible-content marker and introduction copy, but no exact experiment id or config read ties its exposure to this row | Trace the Soundboard NUX renderer to an exact experiment read before adding public analysis. |
| `2026-07-game-mentions-v2-mobile` | the exact mobile experiment is registered with enabled, showNewTag, and combineMentionAutocomplete settings, but the returned config is not assigned or read by a mobile autocomplete surface | Find the mobile game-mention autocomplete component that reads this experiment before writing public analysis. |
| `2026-07-personal-widget` | Add Personal Widget, custom-status, and widget clip-upload flows confirm a visible profile-widget surface, but no exact experiment id or variant consumer links its three treatments | Trace the personal-widget add button or renderer to an exact experiment read and map all three variants. |
| `2026-07-clips-editor-text-track` | no exact experiment id, config object, text-track editor consumer, or linked user-facing string was found in the current bundle | Find a Clips editor text or caption track component tied to this experiment before writing public analysis. |

## 검증 및 커밋/푸시 결과

- JSON 유효성: passed
- 리포트 구조·수량 검증: passed
- history/public 실험 해석 일치: passed (147 rows)
- 한·영 해석 쌍 검증: passed
- unresolved 필드 검증: passed (42 candidates)
- 금지 fallback 문구 검색: passed
- tracked 공개 경로 내용 검사: passed
- 리포트 포인터 일치: passed
- 저장소 테스트: passed (12 tests)
- git diff 검사: passed
- 커밋/푸시: passed (`7a19d2c0374c` pushed to `origin/main`; final metadata recorded by follow-up commit)
- 비고: JSON and report contracts, 147-row history/public interpretation parity, bilingual pairing and English purity, unresolved fields, fallback phrases, tracked publication-path content checks, report pointers, 12 repository tests, and git diff checks passed. The full-checkout scan only reports intentionally ignored local data/history.json and pre-existing .DS_Store files; none is staged or published. No parser or application code changed.

## Security/privacy impact

- 신뢰 경계, 수집·전송·보존·삭제 경로는 바뀌지 않았습니다.
- 공개 변경은 Discord 제품 메타데이터 해석과 집계 리포트뿐이며 개인 데이터, 자격 증명, private runner state를 추가하지 않았습니다.
- 스키마 변경은 없고, 로컬 `data/history.json`은 계속 ignore되어 공개 커밋에 포함되지 않습니다.
