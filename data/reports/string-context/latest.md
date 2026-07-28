# Discord string context report — 2026-07-28

- Generated: `2026-07-28T09:12:22.356Z`
- Period: `2026-07-24T16:47:37Z` to `2026-07-28T06:08:46.953457+00:00`
- Build: `f570ed9078bb26acbe317b9e471d1245b09e50c8`
- Clusters: 11
- Annotated strings: 80
- Deferred: 514
- `latest_changes.json` string_context: not added (current payload has no string rows)

## Outcome

The history window contained 165 string rows. 80 high-value rows were annotated across 11 product clusters; 85 new-window rows and 429 prior carry-forwards remain deferred. The ignored public history snapshot was synchronized to the current f570ed9078bb26acbe317b9e471d1245b09e50c8 source before annotation.

## Annotated clusters

### Game Servers creation, limits, and plan timing

- Keys: `34GMP9`, `6TgadG`, `CrCSF3`, `FEWMXW`, `Yi+FzV`, `xMpGuO`, `yUWVlo`
- Intent: `billing_or_subscription_issue`
- Confidence: `high`
- Rows: 8
- Summary: Discord Shop의 Game Servers에서 서버를 만들고 확인하거나 플랜을 바꿀 때 보이는 문구입니다.
- English: Copy shown when creating, viewing, or changing a hosted game server from Discord's Shop.
- Evidence: 현재 Canary localization과 Game Server Pricing 실험에 생성·관리·플랜·제한 문구가 함께 확인됩니다.

### Nitro profile style presets

- Keys: `4IYwrw`, `M2Hj9s`, `PiPq7M`, `bBRdiB`
- Intent: `feature_or_setting_explanation`
- Confidence: `high`
- Rows: 4
- Summary: Nitro 프로필 스타일을 프리셋으로 미리 보거나 무작위 조합을 시험하는 화면의 라벨입니다.
- English: Labels for previewing a Nitro profile-style preset or trying a random combination of profile customizations.
- Evidence: 현재 Canary 프로필 문자열에서 profile preset, preview, Surprise Me, Nitro customizations가 같은 묶음으로 확인됩니다.

### Waiting for Voice Server connection status

- Keys: `uQle7a`
- Intent: `voice_video_or_device_issue`
- Confidence: `high`
- Rows: 1
- Summary: 음성 채널 연결 중 Discord가 음성 서버 응답을 기다리고 있음을 나타내는 연결 상태입니다.
- English: A connection status indicating that Discord is waiting for the voice server while joining a voice channel.
- Evidence: 현재 Canary 연결 상태 묶음과 같은 시점의 Awaiting Endpoint 삭제가 상태 이름 변경을 뒷받침합니다.

### Vibegrations app editing, shipping, and deletion

- Keys: `4hUJBy`, `6xTawd`, `KV+ICm`, `NkPaHG`, `QDGuNS`, `Z6F624`, `ahRdoJ`, `fYHrcD`, `kvcg+H`, `tqKZCi`, `uAMVJ4`
- Intent: `feature_or_setting_explanation`
- Confidence: `medium`
- Rows: 11
- Summary: Vibegrations 앱 프로젝트의 이름을 바꾸고, 게시하거나, 앱과 작업공간을 삭제하는 제작 화면 문구입니다.
- English: Copy for renaming, publishing, or deleting an app project and its workspace in the Vibegrations creation surface.
- Evidence: 동일 시점의 앱 수명주기 문자열 묶음과 현재 Vibegrations 길드 실험이 같은 제한적 제작 표면을 가리킵니다.

### Custom Typing Indicator

- Keys: `E5VRaj`, `LIcrQP`, `MiMvXU`, `PJmudq`, `ZDK4Nn`, `k6c2yP`, `l8CZ7+`, `lSBp2M`, `oZJRsx`, `pT+BVM`, `uGxDiu`, `yezU3E`
- Intent: `feature_or_setting_explanation`
- Confidence: `medium`
- Rows: 12
- Summary: 기본 입력 중 점 세 개 표시를 이모지·아바타·애니메이션으로 바꾸는 사용자 지정 입력 표시 기능의 문구입니다.
- English: Copy for a Custom Typing Indicator that replaces the default three dots with emojis, an avatar, or animation.
- Evidence: 동일 시점에 기능명, 설명, 이모지·애니메이션 제어, 상대방 노출 안내가 함께 추가되었습니다.

### Nitro reward availability after paid subscription starts

- Keys: `2S/5mX`, `rJbFM3`
- Intent: `billing_or_subscription_issue`
- Confidence: `high`
- Rows: 4
- Summary: 무료 체험 중에는 잠겨 있고 유료 Nitro 구독이 시작된 뒤 받을 수 있는 보상 상태 안내입니다.
- English: A reward status explaining that the item stays locked until the paid Nitro subscription begins.
- Evidence: 동일 시점의 상태·자격 문구와 공개 subscription reward eligibility API 이름이 유료 시작 시점 기준을 뒷받침합니다.

### Nitro free Shop item claim

- Keys: `F7Swt9`, `SlS71X`, `UvLTEv`, `qIVU1h`
- Intent: `billing_or_subscription_issue`
- Confidence: `high`
- Rows: 10
- Summary: Nitro 특전으로 무료 Shop 아이템을 받을 수 있으며 표시된 날짜 전까지 Shop에서 수령하라는 안내입니다.
- English: A Nitro perk notice saying a free Shop item is ready and should be claimed from the Shop by the displayed date.
- Evidence: 현재 Canary의 Nitro Home 문자열에 준비 완료·Shop 이동·수령 기한·특전 목록 문구가 함께 있습니다.

### Overdue message reminders

- Keys: `yBmFPA`
- Intent: `feature_or_setting_explanation`
- Confidence: `high`
- Rows: 2
- Summary: 설정한 확인 시간이 지난 Discord 메시지 리마인더의 개수를 표시하는 문구입니다.
- English: A count of Discord message reminders whose scheduled review time has already passed.
- Evidence: 동일 시점의 overdue count와 기존 Reminders 제목·삭제 동작·Bookmarks 분리 문자열이 같은 기능을 확인합니다.

### Profile Widgets block editor

- Keys: `+VhwRe`, `7bPRjd`, `9AY+/x`, `Li5ivv`, `RyK5Ww`, `fQqXGl`, `g2jVww`, `i3vRzP`, `mZddSK`
- Intent: `feature_or_setting_explanation`
- Confidence: `high`
- Rows: 14
- Summary: Discord 프로필 Board에 위젯 블록을 만들고 필드·이미지·레이아웃을 편집하는 도구의 라벨입니다.
- English: Labels for building Profile Widget blocks and editing their fields, images, and layout on a Discord profile Board.
- Evidence: 현재 Canary Profile Widgets 문자열 묶음에 블록·필드·이미지·레이아웃 편집 라벨이 직접 함께 확인됩니다.

### Clips Gallery and latest clips

- Keys: `JeTeAF`, `zY8Ghg`
- Intent: `feature_or_setting_explanation`
- Confidence: `medium`
- Rows: 2
- Summary: Discord Clips를 모아 보거나 최신 클립을 표시하는 갤러리·목록 라벨입니다.
- English: Gallery and list labels for browsing Discord Clips or showing the latest captured clips.
- Evidence: 현재 Canary에서 Clips Gallery가 Profile Widgets 문자열 옆에 있고, 기존 Clips API·실험 및 최신 클립 문구가 같은 기능명을 뒷받침합니다.

### Call of Duty: MW4 Nitro Reward

- Keys: `+FvISQ`, `6vVfeK`, `Dkm10r`, `IcD/7p`, `QzRqcq`, `RuZS+B`, `YJsqDS`, `fcopjf`, `hworR+`, `ieA3V0`, `kL6q6w`, `nsmhS2`
- Intent: `quest_or_reward_status`
- Confidence: `medium`
- Rows: 12
- Summary: Nitro Rewards에서 Call of Duty: MW4 얼리 액세스 베타용 일회성 코드를 받고 사용하는 프로모션 문구입니다.
- English: Promotion copy for claiming and redeeming a one-time Call of Duty: MW4 Early Access Beta code through Nitro Rewards.
- Evidence: 동일 시점의 26개 MW4 보상 문자열이 전체 수령·사용·종료 흐름을 만들며, 공개 Call of Duty 공식 페이지는 베타 일정과 코드 사용 방식을 보조적으로 확인합니다.

## Deferred

- Carry-forward entries rechecked: 429
- New-window entries deferred: 85
- `bulk_deleted_campaign_copy_not_selected`: 169
- `new_window_not_selected_within_run_cap`: 78
- `vibegrations_cluster_cap_not_selected`: 75
- `low_context_label`: 53
- `current_translation_or_copy_not_selected`: 49
- `deleted_without_current_consumer`: 47
- `deleted_campaign_or_copy_not_selected`: 19
- `deleted_replaced_copy`: 11
- `translation_polish_low_search_intent`: 5
- `copy_polish_or_context_not_selected`: 4
- `internal_or_low_public_context`: 2
- `placeholder_low_context`: 1
- `deleted_low_context_label`: 1

Representative low-context carry-forwards remain deferred:

- `93KE7U` (`Duck`): exact product interaction remains unconfirmed.
- `0JYT98` (`{count}개 음향 숨기기`): exact product interaction remains unconfirmed.
- `uNGhdg` (`싫어요`): exact product interaction remains unconfirmed.
- `7iRs51` (`좋아요`): exact product interaction remains unconfirmed.
- `XhROZk` (`or / 또는`): exact product interaction remains unconfirmed.

## Search signals

- Search Console was not used.
- Public search titles and snippets were secondary signals only.
- Official Call of Duty pages confirm the MW4 beta and code-redemption model, but not the scope of a Discord/Nitro offer.
- No relevant official Discord result was found for Custom Typing Indicator or the free Shop item copy.

## Validation and publish

- Status: `passed`
- `passed` — python3 -m json.tool data/web/meta.json
- `passed` — python3 -m json.tool data/web/strings.ko.json
- `passed` — python3 -m json.tool data/web/strings.en.json
- `passed` — python3 -m json.tool data/latest_changes.json
- `passed` — python3 -m json.tool data/reports/string-context/latest.json
- `passed` — python3 -m json.tool data/reports/string-context/2026-07-28.json
- `passed` — python3 -m json.tool data/history.json
- `passed` — 131 source rows imported without core payload changes
- `passed` — 80 selected analysis-row changes
- `passed` — history/source/web full-row and annotation parity
- `passed` — 80-row paired required-field and English-language checks
- `passed` — analysis-only tracked web comparison
- `passed` — scoped private-path, token, SEO, and overclaim scan
- `passed` — report JSON/Markdown pointer parity
- `passed` — compact tracked web JSON
- `passed` — python3 scripts/security_scan.py --root . .
- `passed` — python3 -m unittest discover -s tests -p 'test_*.py'
- `passed` — ./scripts/check_security.sh (private runner)
- `passed` — git diff --check
- `passed` — data commit pushed to origin/main

- Data commit: `267cf502` — Add July 28 string context interpretations (pushed: true)

## Security/privacy impact

No trust boundary, collection field, storage recipient, retention rule, deletion path, or access control changed. This run adds only public product-string interpretation metadata and report artifacts; it does not add Discord user content, identifiers, credentials, private runner state, or new external recipients.
