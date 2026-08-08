# Discord 데이터마이닝 주간 리포트 — 2026-08-08

## 처리 기간과 빌드

- 처리 기간: `2026-08-05T04:13:55Z` ~ `2026-08-08T04:12:08Z`
- build_hash: `81bc864b8fcd44bd9102faba180a4fd63a755ffc`
- 근거 번들: `canary/web.9ecda3d1a691fd4a.js`
- 입력 기준: ignored `data/history.json`을 우선 확인하고 private extraction history 및 tracked `data/web/*`와 대조했습니다. 빠진 실험 1행과 문자열 17행을 동기화했으며, `latest_changes.json`은 현재 빌드 확인을 위한 보조 신호로만 사용했습니다.

## 핵심 요약

- 실험 10행 / 9개 ID, API 0행, 문자열 273행(253개 고유 행)을 검토했습니다.
- 새 해석은 1행, 삭제 맥락 보존은 4행, 근거 보류는 2행, 보존 맥락 없는 삭제는 3행입니다.
- 데스크톱 맞춤법 검사기가 여러 언어 사전을 함께 쓰는 실험을 실제 소비 경로 근거로 새로 해석했습니다.
- 기존 42개 unresolved를 먼저 재검색했고, plan-selection UI redesign과 gift Shop upsell 후보 2개를 추가해 44개를 이월합니다.
- 기존 147개 Codex 해석 행은 raw 갱신 뒤에도 유지됐으며, 현재 5개 행을 추가해 history/web parity 기준 152개가 됩니다.

## 실험 전수 분석 결과

### interpreted

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-05-electron-multilang-spellcheck` | `2026-08-07T00:38:19Z` | added | interpreted | the desktop spellchecker reads the config and switches between single-language detection and a supported multi-dictionary setup |

### deleted context preserved

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-06-nitro-basic-card-color` | `2026-08-05T18:28:56Z` | deleted | deleted_preserved_context | prior behavior-linked Nitro Basic card styling context is preserved on the deletion row |
| `2026-06-nitro-gifting-price-copy-tweaks` | `2026-08-06T20:31:16Z` | deleted | deleted_preserved_context | prior behavior-linked Nitro gift price and duration context is preserved on the deletion row |
| `2026-06-annual-plan-checkout-copy` | `2026-08-06T22:55:31Z` | deleted | deleted_preserved_context | prior behavior-linked annual-plan savings-copy context is preserved on the deletion row |
| `2026-06-soundboard-picker-height` | `2026-08-07T22:42:26Z` | deleted | deleted_preserved_context | prior behavior-linked standalone Soundboard height context is preserved on the deletion row |

### unresolved

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2026-07-plan-select-ui-redesign` | `2026-08-05T21:09:21Z` | added | unresolved_needs_evidence | no exact experiment registration or plan-selection variant consumer was found in the current bundle |
| `2026-08-hide-gift-shop-upsell` | `2026-08-06T19:38:51Z` | added | unresolved_needs_evidence | no exact experiment registration or consumer links this row to a hidden gifting Shop upsell |

### skipped / deletion-only

| ID | 시각 | 상태 | 판단 | 근거 |
|---|---|---|---|---|
| `2025-10-emoji-search-ranking-tweaks` | `2026-08-06T22:03:02Z` | deleted | deletion_only_no_context | ranking flags are present in archived raw config, but no prior evidence-backed interpretation or current consumer was available to preserve |
| `2026-05-frictionless-gdms` | `2026-08-06T22:41:23Z` | deleted | deletion_only_no_context | the reference deletion row has no prior evidence-backed interpretation or current exact consumer |
| `2026-05-frictionless-gdms` | `2026-08-06T22:50:53.182437+00:00` | deleted | deletion_only_no_context | the raw-detail deletion row has an enabled flag but no prior evidence-backed interpretation or current exact consumer |

## 중요한 실험 상세 해석

### 데스크톱 다국어 맞춤법 검사 (`2026-05-electron-multilang-spellcheck`)

기본 상태의 단일 언어 감지와 비교해, 앱 언어와 기기 언어에서 지원되는 여러 맞춤법 사전을 동시에 적용합니다.

- 근거: The desktop spellchecker constructor reads enableElectronMultilangSpellcheck and calls setSpellCheckerLanguages for the enabled treatment.
- 확인 위치: isElectronMultilangSpellcheckEnabled, navigator.languages, setSpellCheckerLanguages, single-locale fallback

## 실험에서 나타나지 않는 변화

| 영역 | 제품 변화 | 근거와 확신도 |
|---|---|---|
| Living Room 공간·좌석·물건 | Living Room이 Left/Right Lounge와 Loft 같은 공간 이름, 창가·의자·방석 같은 자리, 식물·책·노트북 같은 물건, 자리 점유와 사용자 상태를 더 구체적으로 표시합니다. | A coherent bilingual cluster covers room selection, numbered rooms, occupied or full states, seat positions, objects, notes, and per-user activities. (high) |
| 프로필 위젯 배치와 게임 통계 | 프로필의 위젯을 메인·사이드 열에서 재정렬하거나 제거하고, 게임 플레이·게임 통계·개인 위젯을 추가하는 편집 흐름이 확장됐습니다. | New labels describe main and side column positions, reorder/remove actions, widget categories, games being played, game statistics, and personal widget creation. (high) |
| Clips 갤러리와 편집 | 프로필 Clips Gallery에 게임 클립을 추가·삭제·업로드하는 흐름에 제목 편집, 텍스트 또는 이미지 추가, 타임라인 댓글 같은 편집 단서가 더해졌습니다. | Current strings cover Add/Remove Clip, game-only upload, Edit clip title, Add a title, Add text or an image, Text settings, and Timeline comment. (high) |
| 비활성 그룹 DM 정리 | 약 6개월간 비활성인 그룹 DM을 한 번에 최대 1,000개까지 조용히 나가고, 진행 중·속도 제한·실패·완료 상태를 안내하는 정리 흐름이 나타났습니다. | Korean strings form a full cleanup flow with eligibility, bulk selection, silent leaving, progress, prior-job waiting, rate limits, and per-GDM failure. (high) |
| Favorites와 리마인더 한도 | 채널·DM Favorites와 메시지 리마인더의 추가 방법, 사용량, 무료 한도, Nitro 확장 한도, 공간 확보 방법을 설명하는 안내가 보강됐습니다. | Desktop and mobile gestures, management actions, limit meters, limit errors, deletion guidance, and Nitro capacity copy appear together. (high) |
| 연령 확인 실패·재시도·개인정보 안내 | 셀카나 신분증으로 나이를 확인하지 못했을 때 재시도하는 상태, 최소 연령 미달 결과, 셀카 생체 데이터가 기기에서 처리된다는 안내가 추가됐습니다. | The age-verification cluster explicitly covers selfie and ID failure, retry, unavailable methods, minimum-age results, and on-device biometric processing. (high) |
| 프로필 꾸미기·상태·배지 접근성 | 움직이는 아바타, 배너, 테마 색상, 별명 스타일을 미리 보고 현재 값을 확인하는 기능과 사용자 지정 상태 펼치기·접기, 배지 숨기기·순서 변경 라벨이 보강됐습니다. | Paired profile-editor strings and accessibility labels cover preview controls, current values, custom-status expansion, and badge organization. (high) |
| 오디오 장치 전환 제안 | Discord가 새 오디오 장치를 감지해 입력, 출력 또는 둘 다 바꿀지 묻고 권장 장치와 전환 거부 선택을 함께 보여 줍니다. | The Korean device prompt cluster names vendor/model suggestions, input-only, output-only, combined switching, ignore, and do-not-switch actions. (high) |
| 게임 오버레이 입력 제한 | 게임 오버레이가 호환 모드라 키보드 입력을 받을 수 없을 때 검색과 메시지 입력을 막고 게임 밖 Discord로 전환하라고 안내합니다. | Three same-time strings connect compatibility mode, unavailable search, unavailable typing, and the outside-the-game fallback. (high) |
| Quests 정책 제한 | 정책을 위반한 활동 때문에 Discord Quests 접근이 일시 중단됐음을 알리는 제목과 설명이 추가됐습니다. | The notice explicitly names temporary Quest access suspension and policy-violating activity. (high) |
| Shop 구매 가능 상태와 연간 가격 문구 | 친구가 장착한 아이템이 현재 구매 불가임을 알리는 상태가 추가됐고, 연간 플랜의 ‘몇 개월 절약’·‘최고의 가성비’ 문구는 삭제됐습니다. 삭제만으로 결제 화면 제거를 뜻하지는 않습니다. | Item Unavailable for Purchase appears beside Shop This Look context, while annual-plan savings labels were deleted in both languages. (high) |
| 게임 선택·평가 정보 | 게임 검색과 선택, 플레이 중인 게임, 별점·평가 수, 차트·연령 같은 게임 정보 라벨이 추가됐습니다. 현재 변경만으로 하나의 확정된 화면 구조까지는 연결되지 않습니다. | Strings cover Select a game, Games being played, a star-rating accessibility label, Rating, Chart, and Age, but no single route or component was confirmed for the whole cluster. (medium) |
| Soundboard 데스크톱 소개 | 음성 채널에서 모두가 들을 수 있는 소리를 재생한다는 Soundboard 소개 문구가 한국어에 추가됐습니다. 기존 NUX 실험과의 직접 연결은 아직 확인되지 않았습니다. | The localized introduction confirms a visible Soundboard onboarding surface, but the current bundle still lacks an exact experiment linkage. (medium) |
| 활동·외부 앱 권한과 화면 공유 라벨 | 채널 스레드에서 활동이나 외부 앱 사용을 허용하는 권한 문구와 Live·화면 공유 상태 라벨이 추가됐습니다. 동시에 기존 ‘다른 활동 실행 중’ 문구는 삭제됐지만 기능 제거로 단정할 수 없습니다. | Permission copy, Live count, Sharing Screen, and deletion-only activity-conflict strings are related product signals without a confirmed single experiment. (medium) |
| 공통 텍스트 입력 상태 | 텍스트 입력란의 지우기 동작과 문자 수 한도 도달 상태가 공통 UI 라벨로 추가됐습니다. 어느 특정 작성 화면에 먼저 적용되는지는 확인되지 않았습니다. | TEXT_INPUT_CLEAR and CHARACTER_COUNT_LIMIT_REACHED arrive as shared component keys rather than a route-specific flow. (medium) |

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
| `2026-07-shop-this-look` | Shop This Look and an item-unavailable purchase state are visible, but no exact experiment id or config consumer links that surface to this row | Trace the Shop this Look dismissible content to an exact experiment read before adding public analysis. |
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
| `2026-07-nitro-home-header-followup` | Nitro Home and free Shop-item strings changed, but no exact experiment id or header variant consumer was found | Trace the Nitro Home header component and confirm how Variant 0 and Variant 1 change the visible header. |
| `2026-06-hero-shelf-ad-tile` | the row suggests a visible advertising tile, but no exact experiment id, shelf component, route, or treatment consumer was found | Find a rendered shelf or advertising card that reads this experiment before writing public analysis. |
| `2026-07-gdop-discovery` | no exact experiment id, config consumer, route, or visible discovery component was found | Find an exact experiment registration or discovery component that distinguishes Variant 0 from Variant 1. |
| `2026-07-social-layer-storefront-spend-orbs-banner-copy` | time-limited Nitro and Orbs item copy confirms a storefront banner surface, but no exact experiment id or variant consumer links that copy to this row | Trace the social-layer storefront banner renderer to an exact experiment read and compare the two copy variants. |
| `2026-07-call-of-duty-3pp-expired` | the exact experiment is now registered beside the Call of Duty marketing configs, and expiry strings exist, but its returned config is not assigned, exported, or read by the visible reward card | Find an expired-state component that directly reads this experiment before adding public analysis. |
| `2026-07-cod-3pp` | the exact experiment now exports a config helper, but no current caller uses that base helper; only the two sibling marketing experiments are read by the Nitro tab | Find a Call of Duty provider or reward entrypoint that calls the base experiment helper before writing public analysis. |
| `2026-07-wishlist-show-owned-items-last` | wishlist and gifting surfaces exist, but no exact experiment id or owned-item sorting consumer was found | Find the wishlist item sorter and confirm that it reads this experiment before moving owned items to the end. |
| `2026-08-soundboard-desktop-nux` | the current strings now include the desktop Soundboard introduction in Korean, but no exact experiment id or config read ties the NUX exposure to this row | Trace the Soundboard NUX renderer to an exact experiment read before adding public analysis. |
| `2026-07-game-mentions-v2-mobile` | the exact mobile experiment is registered with enabled, showNewTag, and combineMentionAutocomplete settings, but the returned config is not assigned or read by a mobile autocomplete surface | Find the mobile game-mention autocomplete component that reads this experiment before writing public analysis. |
| `2026-07-personal-widget` | personal-widget, game-stat, clip, and column-reordering UI are visible, but no exact experiment id or variant consumer links its three treatments | Trace the personal-widget add button or renderer to an exact experiment read and map all three variants. |
| `2026-07-clips-editor-text-track` | Clips now has title and text-or-image editing copy, but no exact experiment id, config object, or text-track consumer links those controls to this row | Find a Clips editor text or caption track component tied to this experiment before writing public analysis. |
| `2026-07-plan-select-ui-redesign` | Nitro plan-selection and checkout surfaces exist, but the current Canary bundle has no exact experiment id or variant consumer for this redesign row | Find a plan-selection screen that reads this experiment and compare Variant 0 with Variant 1 before writing public analysis. |
| `2026-08-hide-gift-shop-upsell` | gift and Shop purchase surfaces exist, but the current Canary bundle has no exact experiment id or consumer that hides a gift-Shop upsell | Trace the gifting checkout or Shop upsell renderer to an exact experiment read before describing what is hidden. |

## 검증 및 커밋/푸시 결과

- JSON 유효성: passed
- 리포트 계약: passed
- history/public 해석 parity: passed (152 rows)
- 한국어/영어 해석 쌍: passed
- unresolved 필수 필드: passed (44 candidates)
- 금지 fallback 문구: passed
- tracked public content 검사: passed (2 reviewed allowlisted product-metadata findings)
- 리포트 최신 포인터 일치: passed
- 저장소 테스트: passed (12 tests)
- git diff 검사: passed
- 커밋/푸시: passed (`872eb90d97cc` pushed to `origin/main`; final metadata recorded by follow-up commit)

## Security/privacy impact

신뢰 경계, 수집 목적, 공개 필드, 외부 수신자, 보존기간, 삭제 경로, 백업 방식, 접근권한, 스키마는 바뀌지 않았습니다. 이미 공개된 Discord 제품 메타데이터의 해석과 집계 리포트만 추가하며 개인정보, 원본 메시지, 사용자 식별자, 자격증명, 비공개 러너 상태는 게시하지 않습니다.
