# Bayesian-Shannon Translation Engine — Results Artifact
## Corpus: Justin & Lin Mei Hui (林渼惠), 2/20–3/26/2026

### How to read this
- **[H]** = High confidence (entropy < 0.3 bits) — single dominant interpretation
- **[M]** = Medium confidence (0.3-1.0) — clear winner but alternatives exist
- **[L]** = Low confidence (1.0-2.0) — competitive interpretations
- **[?]** = Review needed (≥2.0 bits) — genuinely ambiguous, multiple viable readings
- «word» = token not in dictionary (needs expansion)
- [subject, %] = inferred dropped subject with Bayesian probability

## Statistics
| Metric | Value |
|--------|-------|
| Messages analyzed | 676 |
| Avg entropy | 1.050 bits |
| HIGH confidence | 276 (40%) |
| MEDIUM confidence | 19 (2%) |
| LOW confidence | 220 (32%) |
| REVIEW needed | 161 (23%) |

---
## Section 1: Messages Flagged for Review (H ≥ 2.0)
*These are the sentences where the Bayesian engine found genuine ambiguity.*

### [2/20 None]
**Chinese:** 我到時候跟我的好朋友他們要照片我發給你，你看你喜歡哪一個
**Primary (H=2.32):** I arrive «時候» «跟» I good friend they «要» «照片» I «發給» you «，» you look/see you like «哪» «一個»
**Alternatives:**
  1. (14%) I arrive «時候» «跟» I good friend they «要» «照片» I «發給» you «，» you look/see you like «哪» «一個»
  2. (14%) I succeed «時候» «跟» I good friend they «要» «照片» I «發給» you «，» you look/see you like «哪» «一個»
  3. (14%) I arrive «時候» «跟» I ok/agreed friend they «要» «照片» I «發給» you «，» you look/see you like «哪» «一個»
  4. (14%) I arrive «時候» «跟» I good friend they «要» «照片» I «發給» you «，» you read you like «哪» «一個»
  5. (14%) I arrive «時候» «跟» I good friend they «要» «照片» I «發給» you «，» you visit you like «哪» «一個»
**Ambiguities detected:**
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [2/21 9:47 PM]
**Chinese:** 只要自己覺得開心就怎麼過
**Primary (H=2.00):** «只要» oneself feel/think happy then/just «怎麼»
**Alternatives:**
  1. (25%) «只要» oneself feel/think happy then/just «怎麼»
  2. (25%) «只要» oneself feel/think happy exactly «怎麼»
  3. (25%) «只要» oneself feel/think happy as_soon_as «怎麼»
  4. (25%) «只要» oneself feel/think happy only «怎麼»
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/21 9:47 PM]
**Chinese:** 你還沒受傷之前、的工作性質是做什麼的？
**Primary (H=2.32):** you still no/not «受傷» «之前» «、» work «性質» is/am/are do/make «什麼» «？»
**Alternatives:**
  1. (17%) you still no/not «受傷» «之前» «、» work «性質» is/am/are do/make «什麼» «？»
  2. (17%) you also no/not «受傷» «之前» «、» work «性質» is/am/are do/make «什麼» «？»
  3. (17%) you even no/not «受傷» «之前» «、» work «性質» is/am/are do/make «什麼» «？»
  4. (17%) you fairly no/not «受傷» «之前» «、» work «性質» is/am/are do/make «什麼» «？»
  5. (17%) you still no/not «受傷» «之前» «、» work «性質» is/am/are work_as «什麼» «？»
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)

### [2/21 9:49 AM]
**Chinese:** 不辛苦、我們已經很幸福很幸運、全世界都這麼亂，我們過得還這麼好
**Primary (H=2.32):** not hard/difficult «、» we «已經» «很» «幸福» «很» «幸運» «、» «全世界» «都» «這麼» «亂» «，» we still «這麼» good
**Alternatives:**
  1. (20%) not hard/difficult «、» we «已經» «很» «幸福» «很» «幸運» «、» «全世界» «都» «這麼» «亂» «，» we still «這麼» good
  2. (20%) not hard/difficult «、» we «已經» «很» «幸福» «很» «幸運» «、» «全世界» «都» «這麼» «亂» «，» we also «這麼» good
  3. (20%) not hard/difficult «、» we «已經» «很» «幸福» «很» «幸運» «、» «全世界» «都» «這麼» «亂» «，» we even «這麼» good
  4. (20%) not hard/difficult «、» we «已經» «很» «幸福» «很» «幸運» «、» «全世界» «都» «這麼» «亂» «，» we fairly «這麼» good
  5. (20%) not hard/difficult «、» we «已經» «很» «幸福» «很» «幸運» «、» «全世界» «都» «這麼» «亂» «，» we still «這麼» ok/agreed
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/21 10:13 AM]
**Chinese:** 沒關係，我們這裡很方便，有空就回應你沒空就慢一點回應
**Primary (H=2.32):** [you, 37%] no/not «關» «係» «，» we «這裡» «很» «方便» «，» «有空» then/just «回應» you no/not «空» then/just «慢» «一點» «回應»
**Alternatives:**
  1. (11%) [you, 37%] no/not «關» «係» «，» we «這裡» «很» «方便» «，» «有空» then/just «回應» you no/not «空» then/just «慢» «一點» «回應»
  2. (11%) [you, 37%] no/not «關» «係» «，» we «這裡» «很» «方便» «，» «有空» then/just «回應» you no/not «空» then/just «慢» «一點» «回應»
  3. (11%) [you, 37%] no/not «關» «係» «，» we «這裡» «很» «方便» «，» «有空» then/just «回應» you no/not «空» then/just «慢» «一點» «回應»
  4. (11%) [you, 37%] no/not «關» «係» «，» we «這裡» «很» «方便» «，» «有空» then/just «回應» you no/not «空» then/just «慢» «一點» «回應»
  5. (11%) [you, 37%] no/not «關» «係» «，» we «這裡» «很» «方便» «，» «有空» exactly «回應» you no/not «空» exactly «慢» «一點» «回應»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/21 10:13 AM]
**Chinese:** 沒事，你去睡覺吧
**Primary (H=2.32):** [I, 36%] it's nothing/no problem «，» you go sleep (let's / how about)
**Alternatives:**
  1. (17%) [I, 36%] it's nothing/no problem «，» you go sleep (let's / how about)
  2. (17%) [I, 36%] it's nothing/no problem «，» you go sleep (fine / I suppose)
  3. (17%) [I, 36%] it's nothing/no problem «，» you go sleep (I think / probably)
  4. (17%) [I, 36%] it's nothing/no problem «，» you go sleep (you should)
  5. (17%) [you, 36%] it's nothing/no problem «，» you go sleep (let's / how about)
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **吧**: suggestion: Let's... / How about..., concession: Fine, go ahead / I suppose so, uncertainty: I think so / probably, softened_command: You should... (softened)

### [2/21 4:20 PM]
**Chinese:** 快去吃吧，沒事我們也在吃了
**Primary (H=2.30):** [I, 36%] «快» go eat (let's / how about) «，» it's nothing/no problem we «也» «在» eat [completed]
**Alternatives:**
  1. (22%) [I, 36%] «快» go eat (let's / how about) «，» it's nothing/no problem we «也» «在» eat [completed]
  2. (21%) [you, 36%] «快» go eat (let's / how about) «，» it's nothing/no problem we «也» «在» eat [completed]
  3. (20%) [I, 36%] «快» go eat (let's / how about) «，» it's nothing/no problem we «也» «在» eat [now/changed]
  4. (20%) [I, 36%] «快» go eat (let's / how about) «，» it's nothing/no problem we «也» «在» eat (too much)
  5. (13%) [we, 22%] «快» go eat (let's / how about) «，» it's nothing/no problem we «也» «在» eat [completed]
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly

### [2/22 1:26 PM]
**Chinese:** 你就發英文的就好，我會翻譯
**Primary (H=2.32):** you then/just «發» «英文» then/just good «，» I «會» «翻譯»
**Alternatives:**
  1. (12%) you then/just «發» «英文» then/just good «，» I «會» «翻譯»
  2. (12%) you then/just «發» «英文» then/just good «，» I «會» «翻譯»
  3. (12%) you then/just «發» «英文» then/just good «，» I «會» «翻譯»
  4. (12%) you then/just «發» «英文» then/just good «，» I «會» «翻譯»
  5. (12%) you exactly «發» «英文» exactly good «，» I «會» «翻譯»
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/22 4:22 PM]
**Chinese:** 現在外面開始在下大雪了
**Primary (H=2.30):** [I, 36%] now «外面» «開始» «在» «下» «大雪» [completed]
**Alternatives:**
  1. (22%) [I, 36%] now «外面» «開始» «在» «下» «大雪» [completed]
  2. (21%) [you, 36%] now «外面» «開始» «在» «下» «大雪» [completed]
  3. (20%) [I, 36%] now «外面» «開始» «在» «下» «大雪» [now/changed]
  4. (20%) [I, 36%] now «外面» «開始» «在» «下» «大雪» (too much)
  5. (13%) [we, 22%] now «外面» «開始» «在» «下» «大雪» [completed]
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly

### [2/22 4:22 PM]
**Chinese:** 沒事，你買一些東西回去才不用跑來跑去，外面開車也危險
**Primary (H=2.32):** [I, 36%] it's nothing/no problem «，» you buy «一些» «東西» go back «才» «不用» run come run go «，» «外面» drive «也» «危險»
**Alternatives:**
  1. (15%) [I, 36%] it's nothing/no problem «，» you buy «一些» «東西» go back «才» «不用» run come run go «，» «外面» drive «也» «危險»
  2. (15%) [I, 36%] it's nothing/no problem «，» you buy «一些» «東西» go back «才» «不用» run come run go «，» «外面» drive «也» «危險»
  3. (15%) [I, 36%] it's nothing/no problem «，» you buy «一些» «東西» go back «才» «不用» run come run go «，» «外面» drive «也» «危險»
  4. (15%) [I, 36%] it's nothing/no problem «，» you buy «一些» «東西» go back «才» «不用» go/visit come go/visit go «，» «外面» drive «也» «危險»
  5. (15%) [I, 36%] it's nothing/no problem «，» you buy «一些» «東西» go back «才» «不用» flee come flee go «，» «外面» drive «也» «危險»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **跑**: run: To run, go/visit: To go out/run errands, flee: To flee/escape
  - polysemy on **跑**: run: To run, go/visit: To go out/run errands, flee: To flee/escape

### [2/22 4:22 PM]
**Chinese:** 你要買一些吃的東西回去才不會到時候沒東西吃下雪不要亂亂跑
**Primary (H=2.00):** you «要» buy «一些» eat «東西» go back «才» not «會» arrive «時候» no/not «東西» eat «下雪» «不要» «亂» «亂» run
**Alternatives:**
  1. (25%) you «要» buy «一些» eat «東西» go back «才» not «會» arrive «時候» no/not «東西» eat «下雪» «不要» «亂» «亂» run
  2. (25%) you «要» buy «一些» eat «東西» go back «才» not «會» succeed «時候» no/not «東西» eat «下雪» «不要» «亂» «亂» run
  3. (25%) you «要» buy «一些» eat «東西» go back «才» not «會» arrive «時候» no/not «東西» eat «下雪» «不要» «亂» «亂» go/visit
  4. (25%) you «要» buy «一些» eat «東西» go back «才» not «會» arrive «時候» no/not «東西» eat «下雪» «不要» «亂» «亂» flee
**Ambiguities detected:**
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **跑**: run: To run, go/visit: To go out/run errands, flee: To flee/escape

### [2/22 4:35 PM]
**Chinese:** 這樣很棒，比叫外賣還要健康
**Primary (H=2.00):** «這樣» «很棒» «，» «比» «叫» «外» sell still «要» healthy
**Alternatives:**
  1. (25%) «這樣» «很棒» «，» «比» «叫» «外» sell still «要» healthy
  2. (25%) «這樣» «很棒» «，» «比» «叫» «外» sell also «要» healthy
  3. (25%) «這樣» «很棒» «，» «比» «叫» «外» sell even «要» healthy
  4. (25%) «這樣» «很棒» «，» «比» «叫» «外» sell fairly «要» healthy
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [2/22 4:35 PM]
**Chinese:** 還有在手機上課
**Primary (H=2.29):** [I, 50%] still have «在手» «機上» «課»
**Alternatives:**
  1. (20%) [I, 50%] still have «在手» «機上» «課»
  2. (20%) [I, 50%] also have «在手» «機上» «課»
  3. (20%) [I, 50%] even have «在手» «機上» «課»
  4. (20%) [I, 50%] fairly have «在手» «機上» «課»
  5. (11%) [we, 28%] still have «在手» «機上» «課»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [2/22 4:35 PM]
**Chinese:** 因為我到時候要在紐約開我帶的這一種產品
**Primary (H=2.32):** «因為» I arrive «時候» «要» «在» New York open I bring «這» «一種» product
**Alternatives:**
  1. (12%) «因為» I arrive «時候» «要» «在» New York open I bring «這» «一種» product
  2. (12%) «因為» I succeed «時候» «要» «在» New York open I bring «這» «一種» product
  3. (12%) «因為» I arrive «時候» «要» «在» New York start/operate I bring «這» «一種» product
  4. (12%) «因為» I arrive «時候» «要» «在» New York drive I bring «這» «一種» product
  5. (12%) «因為» I arrive «時候» «要» «在» New York turn_on I bring «這» «一種» product
**Ambiguities detected:**
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **開**: open: To open, start/operate: To start a business/operate, drive: To drive a vehicle, turn_on: To turn on/switch on
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone

### [2/22 4:35 PM]
**Chinese:** 不是它是帶健康的、還有讓人改善循環、讓身體體不阻塞、我們人就會健康
**Primary (H=2.32):** «不是» «它» is/am/are bring healthy «、» still have «讓» «人» improve «循環» «、» «讓» «身» «體體» not «阻塞» «、» we «人» then/just «會» healthy
**Alternatives:**
  1. (11%) «不是» «它» is/am/are bring healthy «、» still have «讓» «人» improve «循環» «、» «讓» «身» «體體» not «阻塞» «、» we «人» then/just «會» healthy
  2. (11%) «不是» «它» is/am/are wear healthy «、» still have «讓» «人» improve «循環» «、» «讓» «身» «體體» not «阻塞» «、» we «人» then/just «會» healthy
  3. (11%) «不是» «它» is/am/are lead/guide healthy «、» still have «讓» «人» improve «循環» «、» «讓» «身» «體體» not «阻塞» «、» we «人» then/just «會» healthy
  4. (11%) «不是» «它» is/am/are bring healthy «、» also have «讓» «人» improve «循環» «、» «讓» «身» «體體» not «阻塞» «、» we «人» then/just «會» healthy
  5. (11%) «不是» «它» is/am/are bring healthy «、» even have «讓» «人» improve «循環» «、» «讓» «身» «體體» not «阻塞» «、» we «人» then/just «會» healthy
**Ambiguities detected:**
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/22 4:35 PM]
**Chinese:** 有空你再進去看看看，這是你們美國版的說明
**Primary (H=2.32):** [I, 36%] «有空» you «再» «進去» «看看» look/see «，» «這» is/am/are you all «美國» «版» «說明»
**Alternatives:**
  1. (15%) [I, 36%] «有空» you «再» «進去» «看看» look/see «，» «這» is/am/are you all «美國» «版» «說明»
  2. (15%) [I, 36%] «有空» you «再» «進去» «看看» read «，» «這» is/am/are you all «美國» «版» «說明»
  3. (15%) [I, 36%] «有空» you «再» «進去» «看看» visit «，» «這» is/am/are you all «美國» «版» «說明»
  4. (15%) [I, 36%] «有空» you «再» «進去» «看看» think/consider «，» «這» is/am/are you all «美國» «版» «說明»
  5. (15%) [I, 36%] «有空» you «再» «進去» «看看» watch «，» «這» is/am/are you all «美國» «版» «說明»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [2/22 4:35 PM]
**Chinese:** 因為在影片的那個醫生、他是在你們美國俄亥俄州開一間針灸診所開了20幾年、他也是這兩年進去了解他這個產品的好處、所以他的病患現在都有用全球吸引力量子環、
**Primary (H=2.32):** «因為» «在» «影片» «那個» «醫生» «、» he is/am/are «在» you all «美國» «俄亥俄州» open «一間» «針» «灸» «診» open [completed] «20» «幾年» «、» he «也» is/am/are «這» «兩年» «進去» «了解» he «這個» product good «處» «、» «所以» he «病患» now «都» «有用» «全球» «吸引力» «量子» «環» «、»
**Alternatives:**
  1. (10%) «因為» «在» «影片» «那個» «醫生» «、» he is/am/are «在» you all «美國» «俄亥俄州» open «一間» «針» «灸» «診» open [completed] «20» «幾年» «、» he «也» is/am/are «這» «兩年» «進去» «了解» he «這個» product good «處» «、» «所以» he «病患» now «都» «有用» «全球» «吸引力» «量子» «環» «、»
  2. (10%) «因為» «在» «影片» «那個» «醫生» «、» he is/am/are «在» you all «美國» «俄亥俄州» open «一間» «針» «灸» «診» open [completed] «20» «幾年» «、» he «也» is/am/are «這» «兩年» «進去» «了解» he «這個» product good «處» «、» «所以» he «病患» now «都» «有用» «全球» «吸引力» «量子» «環» «、»
  3. (10%) «因為» «在» «影片» «那個» «醫生» «、» he is/am/are «在» you all «美國» «俄亥俄州» open «一間» «針» «灸» «診» open [completed] «20» «幾年» «、» he «也» is/am/are «這» «兩年» «進去» «了解» he «這個» product good «處» «、» «所以» he «病患» now «都» «有用» «全球» «吸引力» «量子» «環» «、»
  4. (10%) «因為» «在» «影片» «那個» «醫生» «、» he is/am/are «在» you all «美國» «俄亥俄州» open «一間» «針» «灸» «診» open [completed] «20» «幾年» «、» he «也» is/am/are «這» «兩年» «進去» «了解» he «這個» product good «處» «、» «所以» he «病患» now «都» «有用» «全球» «吸引力» «量子» «環» «、»
  5. (10%) «因為» «在» «影片» «那個» «醫生» «、» he is/am/are «在» you all «美國» «俄亥俄州» open «一間» «針» «灸» «診» open [completed] «20» «幾年» «、» he «也» is/am/are «這» «兩年» «進去» «了解» he «這個» product good «處» «、» «所以» he «病患» now «都» «有用» «全球» «吸引力» «量子» «環» «、»
**Ambiguities detected:**
  - polysemy on **開**: open: To open, start/operate: To start a business/operate, drive: To drive a vehicle, turn_on: To turn on/switch on
  - polysemy on **開**: open: To open, start/operate: To start a business/operate, drive: To drive a vehicle, turn_on: To turn on/switch on
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/22 4:52 PM]
**Chinese:** 它的產品真的很多好處、我的周圍很多朋友都帶得很好，他們都改善了自己的多年的一些老毛病
**Primary (H=2.32):** «它» product «真的» «很多» good «處» «、» I «周圍» «很多» friend «都» bring «很» good «，» they «都» improve [completed] oneself «多年» «一些» «老毛病»
**Alternatives:**
  1. (20%) «它» product «真的» «很多» good «處» «、» I «周圍» «很多» friend «都» bring «很» good «，» they «都» improve [completed] oneself «多年» «一些» «老毛病»
  2. (20%) «它» product «真的» «很多» good «處» «、» I «周圍» «很多» friend «都» bring «很» good «，» they «都» improve [completed] oneself «多年» «一些» «老毛病»
  3. (20%) «它» product «真的» «很多» good «處» «、» I «周圍» «很多» friend «都» wear «很» good «，» they «都» improve [completed] oneself «多年» «一些» «老毛病»
  4. (20%) «它» product «真的» «很多» good «處» «、» I «周圍» «很多» friend «都» lead/guide «很» good «，» they «都» improve [completed] oneself «多年» «一些» «老毛病»
  5. (20%) «它» product «真的» «很多» ok/agreed «處» «、» I «周圍» «很多» friend «都» bring «很» ok/agreed «，» they «都» improve [completed] oneself «多年» «一些» «老毛病»
**Ambiguities detected:**
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/22 4:52 PM]
**Chinese:** 等我有在纽约開始營運的時候、我會買兩三百條產品、來讓所有人體驗、讓他們身體都改善、他們就會跟我一樣做這個產品買賣
**Primary (H=2.32):** I have «在» «纽约» «開始» «營運» «時候» «、» I «會» buy «兩» «三百» «條產品» «、» come «讓» «所有人» «體驗» «、» «讓» they body/health «都» improve «、» they then/just «會» «跟» I do/make «這個» product «買賣»
**Alternatives:**
  1. (17%) I have «在» «纽约» «開始» «營運» «時候» «、» I «會» buy «兩» «三百» «條產品» «、» come «讓» «所有人» «體驗» «、» «讓» they body/health «都» improve «、» they then/just «會» «跟» I do/make «這個» product «買賣»
  2. (17%) I have «在» «纽约» «開始» «營運» «時候» «、» I «會» buy «兩» «三百» «條產品» «、» come «讓» «所有人» «體驗» «、» «讓» they body/health «都» improve «、» they exactly «會» «跟» I do/make «這個» product «買賣»
  3. (17%) I have «在» «纽约» «開始» «營運» «時候» «、» I «會» buy «兩» «三百» «條產品» «、» come «讓» «所有人» «體驗» «、» «讓» they body/health «都» improve «、» they as_soon_as «會» «跟» I do/make «這個» product «買賣»
  4. (17%) I have «在» «纽约» «開始» «營運» «時候» «、» I «會» buy «兩» «三百» «條產品» «、» come «讓» «所有人» «體驗» «、» «讓» they body/health «都» improve «、» they only «會» «跟» I do/make «這個» product «買賣»
  5. (17%) I have «在» «纽约» «開始» «營運» «時候» «、» I «會» buy «兩» «三百» «條產品» «、» come «讓» «所有人» «體驗» «、» «讓» they body/health «都» improve «、» they then/just «會» «跟» I work_as «這個» product «買賣»
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)

### [2/22 4:52 PM]
**Chinese:** 這個不是紋身這個是戴在身上，他就會打通全身穴道
**Primary (H=2.00):** «這個» «不是» «紋身» «這個» is/am/are wear «在» «身上» «，» he then/just «會» «打通» «全身» «穴道»
**Alternatives:**
  1. (25%) «這個» «不是» «紋身» «這個» is/am/are wear «在» «身上» «，» he then/just «會» «打通» «全身» «穴道»
  2. (25%) «這個» «不是» «紋身» «這個» is/am/are wear «在» «身上» «，» he exactly «會» «打通» «全身» «穴道»
  3. (25%) «這個» «不是» «紋身» «這個» is/am/are wear «在» «身上» «，» he as_soon_as «會» «打通» «全身» «穴道»
  4. (25%) «這個» «不是» «紋身» «這個» is/am/are wear «在» «身上» «，» he only «會» «打通» «全身» «穴道»
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/22 5:29 PM]
**Chinese:** 這個也是你們美國人自己出來分享說他帶了這個產品以後身體都改善了
**Primary (H=2.32):** «這個» «也» is/am/are you all «美國» «人» oneself «出來» «分享» say/speak he bring [completed] «這個» product «以» «後» body/health «都» improve [completed]
**Alternatives:**
  1. (15%) «這個» «也» is/am/are you all «美國» «人» oneself «出來» «分享» say/speak he bring [completed] «這個» product «以» «後» body/health «都» improve [completed]
  2. (15%) «這個» «也» is/am/are you all «美國» «人» oneself «出來» «分享» scold he bring [completed] «這個» product «以» «後» body/health «都» improve [completed]
  3. (15%) «這個» «也» is/am/are you all «美國» «人» oneself «出來» «分享» mean he bring [completed] «這個» product «以» «後» body/health «都» improve [completed]
  4. (15%) «這個» «也» is/am/are you all «美國» «人» oneself «出來» «分享» say/speak he wear [completed] «這個» product «以» «後» body/health «都» improve [completed]
  5. (15%) «這個» «也» is/am/are you all «美國» «人» oneself «出來» «分享» say/speak he lead/guide [completed] «這個» product «以» «後» body/health «都» improve [completed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone

### [2/22 5:29 PM]
**Chinese:** 這兩張圖就是我家人、我的爸爸媽媽還有六個妹妹、五個妹婿、跟一個弟弟、還有他的太太、還有五個嫁出去的妹妹她們的小孩
**Primary (H=2.32):** «這» «兩張» «圖» «就是» «我家» «人» «、» I dad mom still have «六個» younger sister «、» «五個» «妹婿» «、» «跟» «一個» younger brother «、» still have he «太太» «、» still have «五個» «嫁出去» younger sister they «小孩»
**Alternatives:**
  1. (10%) «這» «兩張» «圖» «就是» «我家» «人» «、» I dad mom still have «六個» younger sister «、» «五個» «妹婿» «、» «跟» «一個» younger brother «、» still have he «太太» «、» still have «五個» «嫁出去» younger sister they «小孩»
  2. (10%) «這» «兩張» «圖» «就是» «我家» «人» «、» I dad mom still have «六個» younger sister «、» «五個» «妹婿» «、» «跟» «一個» younger brother «、» still have he «太太» «、» still have «五個» «嫁出去» younger sister they «小孩»
  3. (10%) «這» «兩張» «圖» «就是» «我家» «人» «、» I dad mom still have «六個» younger sister «、» «五個» «妹婿» «、» «跟» «一個» younger brother «、» still have he «太太» «、» still have «五個» «嫁出去» younger sister they «小孩»
  4. (10%) «這» «兩張» «圖» «就是» «我家» «人» «、» I dad mom still have «六個» younger sister «、» «五個» «妹婿» «、» «跟» «一個» younger brother «、» still have he «太太» «、» still have «五個» «嫁出去» younger sister they «小孩»
  5. (10%) «這» «兩張» «圖» «就是» «我家» «人» «、» I dad mom still have «六個» younger sister «、» «五個» «妹婿» «、» «跟» «一個» younger brother «、» still have he «太太» «、» still have «五個» «嫁出去» younger sister they «小孩»
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [2/22 5:29 PM]
**Chinese:** 是的，這是我住在台灣的家人、在我們家拍照、還有一張在餐廳拍的
**Primary (H=2.32):** [I, 36%] is/am/are «，» «這» is/am/are I live «在» Taiwan family «、» «在» we «家» «拍照» «、» still have «一張» «在» «餐廳» «拍»
**Alternatives:**
  1. (17%) [I, 36%] is/am/are «，» «這» is/am/are I live «在» Taiwan family «、» «在» we «家» «拍照» «、» still have «一張» «在» «餐廳» «拍»
  2. (17%) [I, 36%] is/am/are «，» «這» is/am/are I live «在» Taiwan family «、» «在» we «家» «拍照» «、» also have «一張» «在» «餐廳» «拍»
  3. (17%) [I, 36%] is/am/are «，» «這» is/am/are I live «在» Taiwan family «、» «在» we «家» «拍照» «、» even have «一張» «在» «餐廳» «拍»
  4. (17%) [I, 36%] is/am/are «，» «這» is/am/are I live «在» Taiwan family «、» «在» we «家» «拍照» «、» fairly have «一張» «在» «餐廳» «拍»
  5. (17%) [you, 36%] is/am/are «，» «這» is/am/are I live «在» Taiwan family «、» «在» we «家» «拍照» «、» still have «一張» «在» «餐廳» «拍»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [2/22 5:54 PM]
**Chinese:** 我們的家庭雖然是小康家庭、但是我的爸爸媽媽對我們八個小孩特別的好、所以我們很感恩出生在這個大家庭裡、我們也是很幸福有好的爸爸媽媽、還有我們全家大大小小真的很熱鬧
**Primary (H=2.32):** we «家庭» «雖然» is/am/are «小康家庭» «、» «但是» I dad mom right/correct we «八個» «小孩» «特別» good «、» «所以» we «很» «感恩» «出生» «在» «這個» «大家庭» «裡» «、» we «也» is/am/are «很» «幸福» «有好» dad mom «、» still have we «全家» «大大小小» «真的» «很» «熱鬧»
**Alternatives:**
  1. (20%) we «家庭» «雖然» is/am/are «小康家庭» «、» «但是» I dad mom right/correct we «八個» «小孩» «特別» good «、» «所以» we «很» «感恩» «出生» «在» «這個» «大家庭» «裡» «、» we «也» is/am/are «很» «幸福» «有好» dad mom «、» still have we «全家» «大大小小» «真的» «很» «熱鬧»
  2. (20%) we «家庭» «雖然» is/am/are «小康家庭» «、» «但是» I dad mom right/correct we «八個» «小孩» «特別» ok/agreed «、» «所以» we «很» «感恩» «出生» «在» «這個» «大家庭» «裡» «、» we «也» is/am/are «很» «幸福» «有好» dad mom «、» still have we «全家» «大大小小» «真的» «很» «熱鬧»
  3. (20%) we «家庭» «雖然» is/am/are «小康家庭» «、» «但是» I dad mom right/correct we «八個» «小孩» «特別» good «、» «所以» we «很» «感恩» «出生» «在» «這個» «大家庭» «裡» «、» we «也» is/am/are «很» «幸福» «有好» dad mom «、» also have we «全家» «大大小小» «真的» «很» «熱鬧»
  4. (20%) we «家庭» «雖然» is/am/are «小康家庭» «、» «但是» I dad mom right/correct we «八個» «小孩» «特別» good «、» «所以» we «很» «感恩» «出生» «在» «這個» «大家庭» «裡» «、» we «也» is/am/are «很» «幸福» «有好» dad mom «、» even have we «全家» «大大小小» «真的» «很» «熱鬧»
  5. (20%) we «家庭» «雖然» is/am/are «小康家庭» «、» «但是» I dad mom right/correct we «八個» «小孩» «特別» good «、» «所以» we «很» «感恩» «出生» «在» «這個» «大家庭» «裡» «、» we «也» is/am/are «很» «幸福» «有好» dad mom «、» fairly have we «全家» «大大小小» «真的» «很» «熱鬧»
**Ambiguities detected:**
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [2/22 5:54 PM]
**Chinese:** 是的、老天爺對我很好、給我一對好的爸爸媽媽、妹妹跟弟弟、我們的全家人都很善良
**Primary (H=2.29):** [you, 37%] is/am/are «、» «老天» «爺» right/correct I «很» good «、» «給» I «一對» good dad mom «、» younger sister «跟» younger brother «、» we «全家人» «都» «很» kind/good-hearted
**Alternatives:**
  1. (21%) [you, 37%] is/am/are «、» «老天» «爺» right/correct I «很» good «、» «給» I «一對» good dad mom «、» younger sister «跟» younger brother «、» we «全家人» «都» «很» kind/good-hearted
  2. (21%) [you, 37%] is/am/are «、» «老天» «爺» right/correct I «很» good «、» «給» I «一對» good dad mom «、» younger sister «跟» younger brother «、» we «全家人» «都» «很» kind/good-hearted
  3. (21%) [you, 37%] is/am/are «、» «老天» «爺» right/correct I «很» ok/agreed «、» «給» I «一對» ok/agreed dad mom «、» younger sister «跟» younger brother «、» we «全家人» «都» «很» kind/good-hearted
  4. (20%) [I, 36%] is/am/are «、» «老天» «爺» right/correct I «很» good «、» «給» I «一對» good dad mom «、» younger sister «跟» younger brother «、» we «全家人» «都» «很» kind/good-hearted
  5. (12%) [we, 21%] is/am/are «、» «老天» «爺» right/correct I «很» good «、» «給» I «一對» good dad mom «、» younger sister «跟» younger brother «、» we «全家人» «都» «很» kind/good-hearted
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/22 5:54 PM]
**Chinese:** 你放心，我一定會做得特別特別的好、因為這個產品自己會說話、只要戴上身、他們自己反應帶的人都知道、不用我解說、主要是自己的身體狀況，自己知道、所以根本不用我介紹產品，大家就會自己想要自己買自己下去運作
**Primary (H=2.32):** you «放心» «，» I «一定» «會» do/make «特別» «特別» good «、» «因為» «這個» product oneself «會» say/speak «話» «、» «只要» wear «上身» «、» they oneself «反應» bring «人» «都» know «、» «不用» I «解說» «、» «主要» is/am/are oneself body/health «狀況» «，» oneself know «、» «所以» «根本» «不用» I «介紹» product «，» everyone then/just «會» oneself «想要» oneself buy oneself «下去» «運作»
**Alternatives:**
  1. (9%) you «放心» «，» I «一定» «會» do/make «特別» «特別» good «、» «因為» «這個» product oneself «會» say/speak «話» «、» «只要» wear «上身» «、» they oneself «反應» bring «人» «都» know «、» «不用» I «解說» «、» «主要» is/am/are oneself body/health «狀況» «，» oneself know «、» «所以» «根本» «不用» I «介紹» product «，» everyone then/just «會» oneself «想要» oneself buy oneself «下去» «運作»
  2. (9%) you «放心» «，» I «一定» «會» work_as «特別» «特別» good «、» «因為» «這個» product oneself «會» say/speak «話» «、» «只要» wear «上身» «、» they oneself «反應» bring «人» «都» know «、» «不用» I «解說» «、» «主要» is/am/are oneself body/health «狀況» «，» oneself know «、» «所以» «根本» «不用» I «介紹» product «，» everyone then/just «會» oneself «想要» oneself buy oneself «下去» «運作»
  3. (9%) you «放心» «，» I «一定» «會» conduct «特別» «特別» good «、» «因為» «這個» product oneself «會» say/speak «話» «、» «只要» wear «上身» «、» they oneself «反應» bring «人» «都» know «、» «不用» I «解說» «、» «主要» is/am/are oneself body/health «狀況» «，» oneself know «、» «所以» «根本» «不用» I «介紹» product «，» everyone then/just «會» oneself «想要» oneself buy oneself «下去» «運作»
  4. (9%) you «放心» «，» I «一定» «會» do/make «特別» «特別» ok/agreed «、» «因為» «這個» product oneself «會» say/speak «話» «、» «只要» wear «上身» «、» they oneself «反應» bring «人» «都» know «、» «不用» I «解說» «、» «主要» is/am/are oneself body/health «狀況» «，» oneself know «、» «所以» «根本» «不用» I «介紹» product «，» everyone then/just «會» oneself «想要» oneself buy oneself «下去» «運作»
  5. (9%) you «放心» «，» I «一定» «會» do/make «特別» «特別» good «、» «因為» «這個» product oneself «會» scold «話» «、» «只要» wear «上身» «、» they oneself «反應» bring «人» «都» know «、» «不用» I «解說» «、» «主要» is/am/are oneself body/health «狀況» «，» oneself know «、» «所以» «根本» «不用» I «介紹» product «，» everyone then/just «會» oneself «想要» oneself buy oneself «下去» «運作»
**Ambiguities detected:**
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/23 12:25 PM]
**Chinese:** 沒關係呀、不上班就可以睡到自然醒、睡覺還要限制時間不是很累嗎？
**Primary (H=2.32):** [you, 56%] no/not «關» «係» «、» not «上班» then/just «可以» «睡» arrive «自然» «醒» «、» sleep still «要» «限制» time «不是» «很» «累» «？»
**Alternatives:**
  1. (10%) [you, 56%] no/not «關» «係» «、» not «上班» then/just «可以» «睡» arrive «自然» «醒» «、» sleep still «要» «限制» time «不是» «很» «累» «？»
  2. (10%) [you, 56%] no/not «關» «係» «、» not «上班» exactly «可以» «睡» arrive «自然» «醒» «、» sleep still «要» «限制» time «不是» «很» «累» «？»
  3. (10%) [you, 56%] no/not «關» «係» «、» not «上班» as_soon_as «可以» «睡» arrive «自然» «醒» «、» sleep still «要» «限制» time «不是» «很» «累» «？»
  4. (10%) [you, 56%] no/not «關» «係» «、» not «上班» only «可以» «睡» arrive «自然» «醒» «、» sleep still «要» «限制» time «不是» «很» «累» «？»
  5. (10%) [you, 56%] no/not «關» «係» «、» not «上班» then/just «可以» «睡» succeed «自然» «醒» «、» sleep still «要» «限制» time «不是» «很» «累» «？»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **嗎**: yes_no_question: Is it? / Did you?, rhetorical: Isn't it obvious?
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [2/23 1:21 PM]
**Chinese:** 這個是我同事的、爸爸媽媽、他的爸爸開刀好、也有帶量子環產品、恢復的很快、她的媽媽也有戴
**Primary (H=2.00):** «這個» is/am/are I coworker «、» dad mom «、» he dad «開刀» good «、» «也» have bring «量子» «環產品» «、» «恢» «很快» «、» she mom «也» have wear
**Alternatives:**
  1. (25%) «這個» is/am/are I coworker «、» dad mom «、» he dad «開刀» good «、» «也» have bring «量子» «環產品» «、» «恢» «很快» «、» she mom «也» have wear
  2. (25%) «這個» is/am/are I coworker «、» dad mom «、» he dad «開刀» ok/agreed «、» «也» have bring «量子» «環產品» «、» «恢» «很快» «、» she mom «也» have wear
  3. (25%) «這個» is/am/are I coworker «、» dad mom «、» he dad «開刀» good «、» «也» have wear «量子» «環產品» «、» «恢» «很快» «、» she mom «也» have wear
  4. (25%) «這個» is/am/are I coworker «、» dad mom «、» he dad «開刀» good «、» «也» have lead/guide «量子» «環產品» «、» «恢» «很快» «、» she mom «也» have wear
**Ambiguities detected:**
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone

### [2/23 1:21 PM]
**Chinese:** 你看這個是手機測試、我們的手機輻射很強、只要把手環拿在手上，你輻射就不見了、
**Primary (H=2.32):** you look/see «這個» is/am/are «手機» «測試» «、» we «手機» «輻射» «很» «強» «、» «只要» «把手» «環» «拿在手上» «，» you «輻射» then/just «不見» [completed] «、»
**Alternatives:**
  1. (10%) you look/see «這個» is/am/are «手機» «測試» «、» we «手機» «輻射» «很» «強» «、» «只要» «把手» «環» «拿在手上» «，» you «輻射» then/just «不見» [completed] «、»
  2. (10%) you read «這個» is/am/are «手機» «測試» «、» we «手機» «輻射» «很» «強» «、» «只要» «把手» «環» «拿在手上» «，» you «輻射» then/just «不見» [completed] «、»
  3. (10%) you visit «這個» is/am/are «手機» «測試» «、» we «手機» «輻射» «很» «強» «、» «只要» «把手» «環» «拿在手上» «，» you «輻射» then/just «不見» [completed] «、»
  4. (10%) you think/consider «這個» is/am/are «手機» «測試» «、» we «手機» «輻射» «很» «強» «、» «只要» «把手» «環» «拿在手上» «，» you «輻射» then/just «不見» [completed] «、»
  5. (10%) you watch «這個» is/am/are «手機» «測試» «、» we «手機» «輻射» «很» «強» «、» «只要» «把手» «環» «拿在手上» «，» you «輻射» then/just «不見» [completed] «、»
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/23 1:34 PM]
**Chinese:** 所以你的意思是說你頸椎受傷、還有你的心臟也有一些微弱，是嗎
**Primary (H=2.32):** «所以» you «意思» is/am/are say/speak you «頸椎» «受傷» «、» still have you «心臟» «也» have «一些» «微弱» «，» is/am/are
**Alternatives:**
  1. (14%) «所以» you «意思» is/am/are say/speak you «頸椎» «受傷» «、» still have you «心臟» «也» have «一些» «微弱» «，» is/am/are
  2. (14%) «所以» you «意思» is/am/are scold you «頸椎» «受傷» «、» still have you «心臟» «也» have «一些» «微弱» «，» is/am/are
  3. (14%) «所以» you «意思» is/am/are mean you «頸椎» «受傷» «、» still have you «心臟» «也» have «一些» «微弱» «，» is/am/are
  4. (14%) «所以» you «意思» is/am/are say/speak you «頸椎» «受傷» «、» also have you «心臟» «也» have «一些» «微弱» «，» is/am/are
  5. (14%) «所以» you «意思» is/am/are say/speak you «頸椎» «受傷» «、» even have you «心臟» «也» have «一些» «微弱» «，» is/am/are
**Ambiguities detected:**
  - particle on **嗎**: yes_no_question: Is it? / Did you?, rhetorical: Isn't it obvious?
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [2/23 1:34 PM]
**Chinese:** 問好了，改天我出貨的時候、我在拿給你體驗、
**Primary (H=2.12):** [I, 36%] «問» good [completed] «，» «改天» I «出貨» «時候» «、» I «在» «拿» «給» you «體驗» «、»
**Alternatives:**
  1. (27%) [I, 36%] «問» good [completed] «，» «改天» I «出貨» «時候» «、» I «在» «拿» «給» you «體驗» «、»
  2. (27%) [I, 36%] «問» ok/agreed [completed] «，» «改天» I «出貨» «時候» «、» I «在» «拿» «給» you «體驗» «、»
  3. (26%) [you, 36%] «問» good [completed] «，» «改天» I «出貨» «時候» «、» I «在» «拿» «給» you «體驗» «、»
  4. (16%) [we, 22%] «問» good [completed] «，» «改天» I «出貨» «時候» «、» I «在» «拿» «給» you «體驗» «、»
  5. (3%) [they, 5%] «問» good [completed] «，» «改天» I «出貨» «時候» «、» I «在» «拿» «給» you «體驗» «、»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/23 1:34 PM]
**Chinese:** 為什麼我想要賣這個產品？是因為我的爸爸媽媽還有我的家人，我周圍的親戚朋友都帶得很好，所以我也希望全世界的人都是平平安安健健康康。
**Primary (H=2.32):** «為» «什麼» I «想要» sell «這個» product «？» is/am/are «因為» I dad mom still have I family «，» I «周圍» «親戚» friend «都» bring «很» good «，» «所以» I «也» hope «全世界» «人» «都» is/am/are «平平安安» «健健康康» «。»
**Alternatives:**
  1. (14%) «為» «什麼» I «想要» sell «這個» product «？» is/am/are «因為» I dad mom still have I family «，» I «周圍» «親戚» friend «都» bring «很» good «，» «所以» I «也» hope «全世界» «人» «都» is/am/are «平平安安» «健健康康» «。»
  2. (14%) «為» «什麼» I «想要» sell «這個» product «？» is/am/are «因為» I dad mom also have I family «，» I «周圍» «親戚» friend «都» bring «很» good «，» «所以» I «也» hope «全世界» «人» «都» is/am/are «平平安安» «健健康康» «。»
  3. (14%) «為» «什麼» I «想要» sell «這個» product «？» is/am/are «因為» I dad mom even have I family «，» I «周圍» «親戚» friend «都» bring «很» good «，» «所以» I «也» hope «全世界» «人» «都» is/am/are «平平安安» «健健康康» «。»
  4. (14%) «為» «什麼» I «想要» sell «這個» product «？» is/am/are «因為» I dad mom fairly have I family «，» I «周圍» «親戚» friend «都» bring «很» good «，» «所以» I «也» hope «全世界» «人» «都» is/am/are «平平安安» «健健康康» «。»
  5. (14%) «為» «什麼» I «想要» sell «這個» product «？» is/am/are «因為» I dad mom still have I family «，» I «周圍» «親戚» friend «都» wear «很» good «，» «所以» I «也» hope «全世界» «人» «都» is/am/are «平平安安» «健健康康» «。»
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/23 1:34 PM]
**Chinese:** 不認識的人，我都會希望他好了、何況你是我們認識的人那肯定我們更希望你平平安安健健康康
**Primary (H=2.12):** [I, 36%] not know/meet «人» «，» I «都» «會» hope he good [completed] «、» «何況» you is/am/are we know/meet «人» «那» «肯定» we «更» hope you «平平安安» «健健康康»
**Alternatives:**
  1. (27%) [I, 36%] not know/meet «人» «，» I «都» «會» hope he good [completed] «、» «何況» you is/am/are we know/meet «人» «那» «肯定» we «更» hope you «平平安安» «健健康康»
  2. (27%) [I, 36%] not know/meet «人» «，» I «都» «會» hope he ok/agreed [completed] «、» «何況» you is/am/are we know/meet «人» «那» «肯定» we «更» hope you «平平安安» «健健康康»
  3. (26%) [you, 36%] not know/meet «人» «，» I «都» «會» hope he good [completed] «、» «何況» you is/am/are we know/meet «人» «那» «肯定» we «更» hope you «平平安安» «健健康康»
  4. (16%) [we, 22%] not know/meet «人» «，» I «都» «會» hope he good [completed] «、» «何況» you is/am/are we know/meet «人» «那» «肯定» we «更» hope you «平平安安» «健健康康»
  5. (3%) [they, 5%] not know/meet «人» «，» I «都» «會» hope he good [completed] «、» «何況» you is/am/are we know/meet «人» «那» «肯定» we «更» hope you «平平安安» «健健康康»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/23 2:14 PM]
**Chinese:** 這些人都是自己帶得很好出來分享的最後一張圖就是說我們人有這個富貴包的話對身體會有這些不好的影響
**Primary (H=2.32):** «這些» «人» «都» is/am/are oneself bring «很好» «出來» «分享» «最» «後» «一張» «圖» «就是» say/speak we «人» have «這個» «富» «貴包» «話» right/correct body/health «會» have «這些» «不好» «影響»
**Alternatives:**
  1. (20%) «這些» «人» «都» is/am/are oneself bring «很好» «出來» «分享» «最» «後» «一張» «圖» «就是» say/speak we «人» have «這個» «富» «貴包» «話» right/correct body/health «會» have «這些» «不好» «影響»
  2. (20%) «這些» «人» «都» is/am/are oneself wear «很好» «出來» «分享» «最» «後» «一張» «圖» «就是» say/speak we «人» have «這個» «富» «貴包» «話» right/correct body/health «會» have «這些» «不好» «影響»
  3. (20%) «這些» «人» «都» is/am/are oneself lead/guide «很好» «出來» «分享» «最» «後» «一張» «圖» «就是» say/speak we «人» have «這個» «富» «貴包» «話» right/correct body/health «會» have «這些» «不好» «影響»
  4. (20%) «這些» «人» «都» is/am/are oneself bring «很好» «出來» «分享» «最» «後» «一張» «圖» «就是» scold we «人» have «這個» «富» «貴包» «話» right/correct body/health «會» have «這些» «不好» «影響»
  5. (20%) «這些» «人» «都» is/am/are oneself bring «很好» «出來» «分享» «最» «後» «一張» «圖» «就是» mean we «人» have «這個» «富» «貴包» «話» right/correct body/health «會» have «這些» «不好» «影響»
**Ambiguities detected:**
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to

### [2/23 2:14 PM]
**Chinese:** 你就在家空空的，翻譯翻譯這些好處的東西多看看多了解
**Primary (H=2.32):** you then/just «在家» «空空» «，» «翻譯» «翻譯» «這些» good «處» «東西» «多» «看看» «多» «了解»
**Alternatives:**
  1. (20%) you then/just «在家» «空空» «，» «翻譯» «翻譯» «這些» good «處» «東西» «多» «看看» «多» «了解»
  2. (20%) you exactly «在家» «空空» «，» «翻譯» «翻譯» «這些» good «處» «東西» «多» «看看» «多» «了解»
  3. (20%) you as_soon_as «在家» «空空» «，» «翻譯» «翻譯» «這些» good «處» «東西» «多» «看看» «多» «了解»
  4. (20%) you only «在家» «空空» «，» «翻譯» «翻譯» «這些» good «處» «東西» «多» «看看» «多» «了解»
  5. (20%) you then/just «在家» «空空» «，» «翻譯» «翻譯» «這些» ok/agreed «處» «東西» «多» «看看» «多» «了解»
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/23 2:14 PM]
**Chinese:** 我跟你分享的這些，你就自己有空就換你來看、
**Primary (H=2.32):** I «跟» you «分享» «這些» «，» you then/just oneself «有空» then/just «換» you «、»
**Alternatives:**
  1. (14%) I «跟» you «分享» «這些» «，» you then/just oneself «有空» then/just «換» you «、»
  2. (14%) I «跟» you «分享» «這些» «，» you then/just oneself «有空» then/just «換» you «、»
  3. (14%) I «跟» you «分享» «這些» «，» you then/just oneself «有空» then/just «換» you «、»
  4. (14%) I «跟» you «分享» «這些» «，» you then/just oneself «有空» then/just «換» you «、»
  5. (14%) I «跟» you «分享» «這些» «，» you exactly oneself «有空» exactly «換» you «、»
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/23 3:48 PM]
**Chinese:** 這個英文跟中文只要一點點意思，聽得懂看得懂就好了
**Primary (H=2.32):** «這個» «英文» «跟» «中文» «只要» «一點點» «意思» «，» «聽» understand «看得懂» then/just good [completed]
**Alternatives:**
  1. (15%) «這個» «英文» «跟» «中文» «只要» «一點點» «意思» «，» «聽» understand «看得懂» then/just good [completed]
  2. (15%) «這個» «英文» «跟» «中文» «只要» «一點點» «意思» «，» «聽» understand «看得懂» exactly good [completed]
  3. (15%) «這個» «英文» «跟» «中文» «只要» «一點點» «意思» «，» «聽» understand «看得懂» as_soon_as good [completed]
  4. (15%) «這個» «英文» «跟» «中文» «只要» «一點點» «意思» «，» «聽» understand «看得懂» only good [completed]
  5. (15%) «這個» «英文» «跟» «中文» «只要» «一點點» «意思» «，» «聽» understand «看得懂» then/just ok/agreed [completed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/23 5:10 PM]
**Chinese:** 我們家就只有我不會煮菜、其她六個妹妹、一個弟弟都會
**Primary (H=2.00):** we «家» then/just «只有» I not «會» «煮菜» «、» «其» she «六個» younger sister «、» «一個» younger brother «都» «會»
**Alternatives:**
  1. (25%) we «家» then/just «只有» I not «會» «煮菜» «、» «其» she «六個» younger sister «、» «一個» younger brother «都» «會»
  2. (25%) we «家» exactly «只有» I not «會» «煮菜» «、» «其» she «六個» younger sister «、» «一個» younger brother «都» «會»
  3. (25%) we «家» as_soon_as «只有» I not «會» «煮菜» «、» «其» she «六個» younger sister «、» «一個» younger brother «都» «會»
  4. (25%) we «家» only «只有» I not «會» «煮菜» «、» «其» she «六個» younger sister «、» «一個» younger brother «都» «會»
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/23 5:33 PM]
**Chinese:** 我們家裡都是做家常菜、媽媽爸爸妹妹他們大家做的都很好吃、我不挑食，因為我不會做菜什麼都是好吃的
**Primary (H=2.32):** we «家裡» «都» is/am/are do/make «家常菜» «、» mom dad younger sister they everyone do/make «都» «很» «好吃» «、» I not «挑食» «，» «因為» I not «會» «做菜» «什麼» «都» is/am/are «好吃»
**Alternatives:**
  1. (20%) we «家裡» «都» is/am/are do/make «家常菜» «、» mom dad younger sister they everyone do/make «都» «很» «好吃» «、» I not «挑食» «，» «因為» I not «會» «做菜» «什麼» «都» is/am/are «好吃»
  2. (20%) we «家裡» «都» is/am/are do/make «家常菜» «、» mom dad younger sister they everyone do/make «都» «很» «好吃» «、» I not «挑食» «，» «因為» I not «會» «做菜» «什麼» «都» is/am/are «好吃»
  3. (20%) we «家裡» «都» is/am/are do/make «家常菜» «、» mom dad younger sister they everyone do/make «都» «很» «好吃» «、» I not «挑食» «，» «因為» I not «會» «做菜» «什麼» «都» is/am/are «好吃»
  4. (20%) we «家裡» «都» is/am/are work_as «家常菜» «、» mom dad younger sister they everyone work_as «都» «很» «好吃» «、» I not «挑食» «，» «因為» I not «會» «做菜» «什麼» «都» is/am/are «好吃»
  5. (20%) we «家裡» «都» is/am/are conduct «家常菜» «、» mom dad younger sister they everyone conduct «都» «很» «好吃» «、» I not «挑食» «，» «因為» I not «會» «做菜» «什麼» «都» is/am/are «好吃»
**Ambiguities detected:**
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)

### [2/23 6:29 PM]
**Chinese:** 我只有在台灣吃過、還有纽约也有賣
**Primary (H=2.00):** I «只有» «在» Taiwan eat «、» still have «纽约» «也» have sell
**Alternatives:**
  1. (25%) I «只有» «在» Taiwan eat «、» still have «纽约» «也» have sell
  2. (25%) I «只有» «在» Taiwan eat «、» also have «纽约» «也» have sell
  3. (25%) I «只有» «在» Taiwan eat «、» even have «纽约» «也» have sell
  4. (25%) I «只有» «在» Taiwan eat «、» fairly have «纽约» «也» have sell
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [2/23 6:29 PM]
**Chinese:** 其他地方我沒看過也沒吃過
**Primary (H=2.32):** «其他» «地方» I no/not look/see «也» no/not eat
**Alternatives:**
  1. (20%) «其他» «地方» I no/not look/see «也» no/not eat
  2. (20%) «其他» «地方» I no/not read «也» no/not eat
  3. (20%) «其他» «地方» I no/not visit «也» no/not eat
  4. (20%) «其他» «地方» I no/not think/consider «也» no/not eat
  5. (20%) «其他» «地方» I no/not watch «也» no/not eat
**Ambiguities detected:**
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [2/24 11:22 AM]
**Chinese:** 我們九點就吃早餐了、你也快去吃早餐
**Primary (H=2.00):** we «九點» then/just eat breakfast [completed] «、» you «也» «快» go eat breakfast
**Alternatives:**
  1. (25%) we «九點» then/just eat breakfast [completed] «、» you «也» «快» go eat breakfast
  2. (25%) we «九點» exactly eat breakfast [completed] «、» you «也» «快» go eat breakfast
  3. (25%) we «九點» as_soon_as eat breakfast [completed] «、» you «也» «快» go eat breakfast
  4. (25%) we «九點» only eat breakfast [completed] «、» you «也» «快» go eat breakfast
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/24 12:22 PM]
**Chinese:** 是的，老天爺對我們全家都很好、全世界這麼大能夠有緣分當家人、還有當朋友也是不容易的、
**Primary (H=2.32):** [I, 50%] is/am/are «，» «老天» «爺» right/correct we «全家» «都» «很» good «、» «全世界» «這麼» «大» «能» «夠» have «緣» «分當» family «、» still have «當» friend «也» is/am/are not «容易» «、»
**Alternatives:**
  1. (17%) [I, 50%] is/am/are «，» «老天» «爺» right/correct we «全家» «都» «很» good «、» «全世界» «這麼» «大» «能» «夠» have «緣» «分當» family «、» still have «當» friend «也» is/am/are not «容易» «、»
  2. (17%) [I, 50%] is/am/are «，» «老天» «爺» right/correct we «全家» «都» «很» ok/agreed «、» «全世界» «這麼» «大» «能» «夠» have «緣» «分當» family «、» still have «當» friend «也» is/am/are not «容易» «、»
  3. (17%) [I, 50%] is/am/are «，» «老天» «爺» right/correct we «全家» «都» «很» good «、» «全世界» «這麼» «大» «能» «夠» have «緣» «分當» family «、» also have «當» friend «也» is/am/are not «容易» «、»
  4. (17%) [I, 50%] is/am/are «，» «老天» «爺» right/correct we «全家» «都» «很» good «、» «全世界» «這麼» «大» «能» «夠» have «緣» «分當» family «、» even have «當» friend «也» is/am/are not «容易» «、»
  5. (17%) [I, 50%] is/am/are «，» «老天» «爺» right/correct we «全家» «都» «很» good «、» «全世界» «這麼» «大» «能» «夠» have «緣» «分當» family «、» fairly have «當» friend «也» is/am/are not «容易» «、»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [2/24 1:03 PM]
**Chinese:** 老天爺、對我超級好、因為我們只要抱著善良的心不去害人、別人要害我們就當成來還債、這樣子就一直會遇到貴人幫忙
**Primary (H=2.32):** «老天» «爺» «、» right/correct I «超級» good «、» «因為» we «只要» «抱著» kind/good-hearted «心» not go «害人» «、» «別人» «要害» we then/just «當» «成來» «還債» «、» «這樣» «子» then/just «一直» «會» «遇到» «貴人» help
**Alternatives:**
  1. (12%) «老天» «爺» «、» right/correct I «超級» good «、» «因為» we «只要» «抱著» kind/good-hearted «心» not go «害人» «、» «別人» «要害» we then/just «當» «成來» «還債» «、» «這樣» «子» then/just «一直» «會» «遇到» «貴人» help
  2. (12%) «老天» «爺» «、» right/correct I «超級» ok/agreed «、» «因為» we «只要» «抱著» kind/good-hearted «心» not go «害人» «、» «別人» «要害» we then/just «當» «成來» «還債» «、» «這樣» «子» then/just «一直» «會» «遇到» «貴人» help
  3. (12%) «老天» «爺» «、» right/correct I «超級» good «、» «因為» we «只要» «抱著» kind/good-hearted «心» not go «害人» «、» «別人» «要害» we then/just «當» «成來» «還債» «、» «這樣» «子» then/just «一直» «會» «遇到» «貴人» help
  4. (12%) «老天» «爺» «、» right/correct I «超級» good «、» «因為» we «只要» «抱著» kind/good-hearted «心» not go «害人» «、» «別人» «要害» we then/just «當» «成來» «還債» «、» «這樣» «子» then/just «一直» «會» «遇到» «貴人» help
  5. (12%) «老天» «爺» «、» right/correct I «超級» good «、» «因為» we «只要» «抱著» kind/good-hearted «心» not go «害人» «、» «別人» «要害» we then/just «當» «成來» «還債» «、» «這樣» «子» then/just «一直» «會» «遇到» «貴人» help
**Ambiguities detected:**
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/24 5:26 PM]
**Chinese:** 沒事、這裡老闆娘都是預約的，所以不怎麼忙別擔心、你要找時間正常吃飯、累了就去睡覺
**Primary (H=2.26):** [you, 56%] it's nothing/no problem «、» «這裡» «老» «闆» «娘» «都» is/am/are «預» «約» «，» «所以» not «怎麼» «忙別» «擔心» «、» you «要» «找» time «正常» eat rice/meal «、» «累» [completed] then/just go «睡» «覺»
**Alternatives:**
  1. (21%) [you, 56%] it's nothing/no problem «、» «這裡» «老» «闆» «娘» «都» is/am/are «預» «約» «，» «所以» not «怎麼» «忙別» «擔心» «、» you «要» «找» time «正常» eat rice/meal «、» «累» [completed] then/just go «睡» «覺»
  2. (21%) [you, 56%] it's nothing/no problem «、» «這裡» «老» «闆» «娘» «都» is/am/are «預» «約» «，» «所以» not «怎麼» «忙別» «擔心» «、» you «要» «找» time «正常» eat rice/meal «、» «累» [completed] exactly go «睡» «覺»
  3. (21%) [you, 56%] it's nothing/no problem «、» «這裡» «老» «闆» «娘» «都» is/am/are «預» «約» «，» «所以» not «怎麼» «忙別» «擔心» «、» you «要» «找» time «正常» eat rice/meal «、» «累» [completed] as_soon_as go «睡» «覺»
  4. (21%) [you, 56%] it's nothing/no problem «、» «這裡» «老» «闆» «娘» «都» is/am/are «預» «約» «，» «所以» not «怎麼» «忙別» «擔心» «、» you «要» «找» time «正常» eat rice/meal «、» «累» [completed] only go «睡» «覺»
  5. (8%) [I, 22%] it's nothing/no problem «、» «這裡» «老» «闆» «娘» «都» is/am/are «預» «約» «，» «所以» not «怎麼» «忙別» «擔心» «、» you «要» «找» time «正常» eat rice/meal «、» «累» [completed] then/just go «睡» «覺»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/25 10:57 AM]
**Chinese:** 哈哈、那麼我就太厲害了
**Primary (H=2.32):** «哈哈» «、» «那麼» I then/just «太» impressive [completed]
**Alternatives:**
  1. (17%) «哈哈» «、» «那麼» I then/just «太» impressive [completed]
  2. (17%) «哈哈» «、» «那麼» I exactly «太» impressive [completed]
  3. (17%) «哈哈» «、» «那麼» I as_soon_as «太» impressive [completed]
  4. (17%) «哈哈» «、» «那麼» I only «太» impressive [completed]
  5. (16%) «哈哈» «、» «那麼» I then/just «太» impressive [now/changed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/25 12:46 PM]
**Chinese:** 沒事、我們也剛剛忙好一對夫妻
**Primary (H=2.12):** [you, 37%] it's nothing/no problem «、» we «也» «剛剛» busy good «一對» «夫妻»
**Alternatives:**
  1. (27%) [you, 37%] it's nothing/no problem «、» we «也» «剛剛» busy good «一對» «夫妻»
  2. (27%) [you, 37%] it's nothing/no problem «、» we «也» «剛剛» busy ok/agreed «一對» «夫妻»
  3. (26%) [I, 36%] it's nothing/no problem «、» we «也» «剛剛» busy good «一對» «夫妻»
  4. (15%) [we, 21%] it's nothing/no problem «、» we «也» «剛剛» busy good «一對» «夫妻»
  5. (3%) [they, 5%] it's nothing/no problem «、» we «也» «剛剛» busy good «一對» «夫妻»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [2/25 8:00 PM]
**Chinese:** 你這個是什麼？看起來真好吃。
**Primary (H=2.32):** you «這個» is/am/are «什麼» «？» look/see «起來» «真» «好吃» «。»
**Alternatives:**
  1. (20%) you «這個» is/am/are «什麼» «？» look/see «起來» «真» «好吃» «。»
  2. (20%) you «這個» is/am/are «什麼» «？» read «起來» «真» «好吃» «。»
  3. (20%) you «這個» is/am/are «什麼» «？» visit «起來» «真» «好吃» «。»
  4. (20%) you «這個» is/am/are «什麼» «？» think/consider «起來» «真» «好吃» «。»
  5. (20%) you «這個» is/am/are «什麼» «？» watch «起來» «真» «好吃» «。»
**Ambiguities detected:**
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [2/26 11:09 AM]
**Chinese:** 快去吃早餐吧
**Primary (H=2.32):** [you, 37%] «快» go eat breakfast (let's / how about)
**Alternatives:**
  1. (18%) [you, 37%] «快» go eat breakfast (let's / how about)
  2. (17%) [you, 37%] «快» go eat breakfast (fine / I suppose)
  3. (17%) [you, 37%] «快» go eat breakfast (I think / probably)
  4. (17%) [you, 37%] «快» go eat breakfast (you should)
  5. (17%) [I, 36%] «快» go eat breakfast (let's / how about)
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **吧**: suggestion: Let's... / How about..., concession: Fine, go ahead / I suppose so, uncertainty: I think so / probably, softened_command: You should... (softened)

### [2/26 4:19 PM]
**Chinese:** 等紐約開
**Primary (H=2.32):** New York open
**Alternatives:**
  1. (20%) New York open
  2. (20%) New York start/operate
  3. (20%) New York drive
  4. (20%) New York turn_on
  5. (20%) New York prescribe
**Ambiguities detected:**
  - polysemy on **開**: open: To open, start/operate: To start a business/operate, drive: To drive a vehicle, turn_on: To turn on/switch on

### [2/27 2:06 PM]
**Chinese:** 是的，規劃是好事、問題是現在大環境不允許亂投資、身上有錢就有安全感、再看看大環境再決定不著急
**Primary (H=2.32):** [you, 37%] is/am/are «，» «規劃» is/am/are «好事» «、» «問題» is/am/are now «大» «環境» not «允許» «亂» «投資» «、» «身上» have money then/just have «安全感» «、» «再» «看看» «大» «環境» «再» «決定» «不著» «急»
**Alternatives:**
  1. (17%) [you, 37%] is/am/are «，» «規劃» is/am/are «好事» «、» «問題» is/am/are now «大» «環境» not «允許» «亂» «投資» «、» «身上» have money then/just have «安全感» «、» «再» «看看» «大» «環境» «再» «決定» «不著» «急»
  2. (17%) [you, 37%] is/am/are «，» «規劃» is/am/are «好事» «、» «問題» is/am/are now «大» «環境» not «允許» «亂» «投資» «、» «身上» have money exactly have «安全感» «、» «再» «看看» «大» «環境» «再» «決定» «不著» «急»
  3. (17%) [you, 37%] is/am/are «，» «規劃» is/am/are «好事» «、» «問題» is/am/are now «大» «環境» not «允許» «亂» «投資» «、» «身上» have money as_soon_as have «安全感» «、» «再» «看看» «大» «環境» «再» «決定» «不著» «急»
  4. (17%) [you, 37%] is/am/are «，» «規劃» is/am/are «好事» «、» «問題» is/am/are now «大» «環境» not «允許» «亂» «投資» «、» «身上» have money only have «安全感» «、» «再» «看看» «大» «環境» «再» «決定» «不著» «急»
  5. (17%) [I, 36%] is/am/are «，» «規劃» is/am/are «好事» «、» «問題» is/am/are now «大» «環境» not «允許» «亂» «投資» «、» «身上» have money then/just have «安全感» «、» «再» «看看» «大» «環境» «再» «決定» «不著» «急»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/28 10:04 AM]
**Chinese:** 因為早餐簡單，我從小到大就會每天吃兩顆水煮蛋、一個牛油果、加一點堅果類、是必備的、
**Primary (H=2.32):** «因為» breakfast simple «，» I «從» «小» arrive «大» then/just «會» «每天» eat «兩顆» boiled egg «、» «一個» avocado «、» «加» «一點» nuts «類» «、» is/am/are «必備» «、»
**Alternatives:**
  1. (20%) «因為» breakfast simple «，» I «從» «小» arrive «大» then/just «會» «每天» eat «兩顆» boiled egg «、» «一個» avocado «、» «加» «一點» nuts «類» «、» is/am/are «必備» «、»
  2. (20%) «因為» breakfast simple «，» I «從» «小» succeed «大» then/just «會» «每天» eat «兩顆» boiled egg «、» «一個» avocado «、» «加» «一點» nuts «類» «、» is/am/are «必備» «、»
  3. (20%) «因為» breakfast simple «，» I «從» «小» arrive «大» exactly «會» «每天» eat «兩顆» boiled egg «、» «一個» avocado «、» «加» «一點» nuts «類» «、» is/am/are «必備» «、»
  4. (20%) «因為» breakfast simple «，» I «從» «小» arrive «大» as_soon_as «會» «每天» eat «兩顆» boiled egg «、» «一個» avocado «、» «加» «一點» nuts «類» «、» is/am/are «必備» «、»
  5. (20%) «因為» breakfast simple «，» I «從» «小» arrive «大» only «會» «每天» eat «兩顆» boiled egg «、» «一個» avocado «、» «加» «一點» nuts «類» «、» is/am/are «必備» «、»
**Ambiguities detected:**
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/28 10:04 AM]
**Chinese:** 有時候早餐就搭配cheese麵包、或者搭配南瓜小米粥、或者山藥小米粥、
**Primary (H=2.32):** [I, 36%] have «時候» breakfast then/just «搭配» «cheese» «麵» «包» «、» «或者» «搭配» «南瓜» «小米粥» «、» «或者» «山藥» «小米粥» «、»
**Alternatives:**
  1. (17%) [I, 36%] have «時候» breakfast then/just «搭配» «cheese» «麵» «包» «、» «或者» «搭配» «南瓜» «小米粥» «、» «或者» «山藥» «小米粥» «、»
  2. (17%) [I, 36%] have «時候» breakfast exactly «搭配» «cheese» «麵» «包» «、» «或者» «搭配» «南瓜» «小米粥» «、» «或者» «山藥» «小米粥» «、»
  3. (17%) [I, 36%] have «時候» breakfast as_soon_as «搭配» «cheese» «麵» «包» «、» «或者» «搭配» «南瓜» «小米粥» «、» «或者» «山藥» «小米粥» «、»
  4. (17%) [I, 36%] have «時候» breakfast only «搭配» «cheese» «麵» «包» «、» «或者» «搭配» «南瓜» «小米粥» «、» «或者» «山藥» «小米粥» «、»
  5. (17%) [you, 36%] have «時候» breakfast then/just «搭配» «cheese» «麵» «包» «、» «或者» «搭配» «南瓜» «小米粥» «、» «或者» «山藥» «小米粥» «、»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/28 10:04 AM]
**Chinese:** 我就只會這些系列的、其它不會
**Primary (H=2.00):** I then/just «只» «會» «這些» «系列» «、» «其它» not «會»
**Alternatives:**
  1. (25%) I then/just «只» «會» «這些» «系列» «、» «其它» not «會»
  2. (25%) I exactly «只» «會» «這些» «系列» «、» «其它» not «會»
  3. (25%) I as_soon_as «只» «會» «這些» «系列» «、» «其它» not «會»
  4. (25%) I only «只» «會» «這些» «系列» «、» «其它» not «會»
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [2/28 11:17 AM]
**Chinese:** 水煮蛋很簡單、只要你的水先煮滾了，再把雞蛋放進去讓他煮10分鐘、把蛋撈出來泡冷水就OK了
**Primary (H=2.32):** boiled egg «很» simple «、» «只要» you water «先» cook «滾» [completed] «，» «再» «把» «雞蛋» «放進» go «讓» he cook «10» «分鐘» «、» «把» «蛋» «撈» «出來» «泡» «冷水» then/just «OK» [completed]
**Alternatives:**
  1. (17%) boiled egg «很» simple «、» «只要» you water «先» cook «滾» [completed] «，» «再» «把» «雞蛋» «放進» go «讓» he cook «10» «分鐘» «、» «把» «蛋» «撈» «出來» «泡» «冷水» then/just «OK» [completed]
  2. (17%) boiled egg «很» simple «、» «只要» you water «先» cook «滾» [completed] «，» «再» «把» «雞蛋» «放進» go «讓» he cook «10» «分鐘» «、» «把» «蛋» «撈» «出來» «泡» «冷水» exactly «OK» [completed]
  3. (17%) boiled egg «很» simple «、» «只要» you water «先» cook «滾» [completed] «，» «再» «把» «雞蛋» «放進» go «讓» he cook «10» «分鐘» «、» «把» «蛋» «撈» «出來» «泡» «冷水» as_soon_as «OK» [completed]
  4. (17%) boiled egg «很» simple «、» «只要» you water «先» cook «滾» [completed] «，» «再» «把» «雞蛋» «放進» go «讓» he cook «10» «分鐘» «、» «把» «蛋» «撈» «出來» «泡» «冷水» only «OK» [completed]
  5. (16%) boiled egg «很» simple «、» «只要» you water «先» cook «滾» [now/changed] «，» «再» «把» «雞蛋» «放進» go «讓» he cook «10» «分鐘» «、» «把» «蛋» «撈» «出來» «泡» «冷水» then/just «OK» [now/changed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/1 11:34 AM]
**Chinese:** 好的謝謝你
**Primary (H=2.12):** [you, 37%] good thank you you
**Alternatives:**
  1. (27%) [you, 37%] good thank you you
  2. (27%) [you, 37%] ok/agreed thank you you
  3. (26%) [I, 36%] good thank you you
  4. (15%) [we, 21%] good thank you you
  5. (3%) [they, 5%] good thank you you
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/1 3:44 PM]
**Chinese:** 閱讀是好事、有空閒我還是會閱讀、
**Primary (H=2.29):** [I, 50%] «閱讀» is/am/are «好事» «、» «有空» «閒» I still is/am/are «會» «閱讀» «、»
**Alternatives:**
  1. (20%) [I, 50%] «閱讀» is/am/are «好事» «、» «有空» «閒» I still is/am/are «會» «閱讀» «、»
  2. (20%) [I, 50%] «閱讀» is/am/are «好事» «、» «有空» «閒» I also is/am/are «會» «閱讀» «、»
  3. (20%) [I, 50%] «閱讀» is/am/are «好事» «、» «有空» «閒» I even is/am/are «會» «閱讀» «、»
  4. (20%) [I, 50%] «閱讀» is/am/are «好事» «、» «有空» «閒» I fairly is/am/are «會» «閱讀» «、»
  5. (11%) [we, 28%] «閱讀» is/am/are «好事» «、» «有空» «閒» I still is/am/are «會» «閱讀» «、»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/2 11:33 AM]
**Chinese:** 從小到大，我都是躺下，1分鐘就睡著了、馬上叫馬上起床，我也不賴床的習慣
**Primary (H=2.32):** [I, 50%] «從» «小» arrive «大» «，» I «都» is/am/are «躺» «下» «，» «1» «分鐘» then/just «睡著» [completed] «、» «馬» «上» «叫» «馬» «上» wake up «，» I «也» «不賴» «床» «習慣»
**Alternatives:**
  1. (17%) [I, 50%] «從» «小» arrive «大» «，» I «都» is/am/are «躺» «下» «，» «1» «分鐘» then/just «睡著» [completed] «、» «馬» «上» «叫» «馬» «上» wake up «，» I «也» «不賴» «床» «習慣»
  2. (17%) [I, 50%] «從» «小» succeed «大» «，» I «都» is/am/are «躺» «下» «，» «1» «分鐘» then/just «睡著» [completed] «、» «馬» «上» «叫» «馬» «上» wake up «，» I «也» «不賴» «床» «習慣»
  3. (17%) [I, 50%] «從» «小» arrive «大» «，» I «都» is/am/are «躺» «下» «，» «1» «分鐘» exactly «睡著» [completed] «、» «馬» «上» «叫» «馬» «上» wake up «，» I «也» «不賴» «床» «習慣»
  4. (17%) [I, 50%] «從» «小» arrive «大» «，» I «都» is/am/are «躺» «下» «，» «1» «分鐘» as_soon_as «睡著» [completed] «、» «馬» «上» «叫» «馬» «上» wake up «，» I «也» «不賴» «床» «習慣»
  5. (17%) [I, 50%] «從» «小» arrive «大» «，» I «都» is/am/are «躺» «下» «，» «1» «分鐘» only «睡著» [completed] «、» «馬» «上» «叫» «馬» «上» wake up «，» I «也» «不賴» «床» «習慣»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/2 12:02 PM]
**Chinese:** 你們美國的保險費、還不錯
**Primary (H=2.00):** you all «美國» «保險» «費» «、» still «不錯»
**Alternatives:**
  1. (25%) you all «美國» «保險» «費» «、» still «不錯»
  2. (25%) you all «美國» «保險» «費» «、» also «不錯»
  3. (25%) you all «美國» «保險» «費» «、» even «不錯»
  4. (25%) you all «美國» «保險» «費» «、» fairly «不錯»
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/2 12:18 PM]
**Chinese:** 老天爺都是對我們好人好
**Primary (H=2.12):** [you, 37%] «老天» «爺» «都» is/am/are right/correct we «好人» good
**Alternatives:**
  1. (27%) [you, 37%] «老天» «爺» «都» is/am/are right/correct we «好人» good
  2. (27%) [you, 37%] «老天» «爺» «都» is/am/are right/correct we «好人» ok/agreed
  3. (26%) [I, 36%] «老天» «爺» «都» is/am/are right/correct we «好人» good
  4. (15%) [we, 21%] «老天» «爺» «都» is/am/are right/correct we «好人» good
  5. (3%) [they, 5%] «老天» «爺» «都» is/am/are right/correct we «好人» good
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/2 7:57 PM]
**Chinese:** 報稅扣款還沒開始，我只是先把錢放進去、讓他可以來得及扣款就好
**Primary (H=2.32):** «報稅» «扣款» still no/not «開始» «，» I «只是» «先» «把» money «放» «進去» «、» «讓» he «可以» «來得» «及» «扣款» then/just good
**Alternatives:**
  1. (12%) «報稅» «扣款» still no/not «開始» «，» I «只是» «先» «把» money «放» «進去» «、» «讓» he «可以» «來得» «及» «扣款» then/just good
  2. (12%) «報稅» «扣款» also no/not «開始» «，» I «只是» «先» «把» money «放» «進去» «、» «讓» he «可以» «來得» «及» «扣款» then/just good
  3. (12%) «報稅» «扣款» even no/not «開始» «，» I «只是» «先» «把» money «放» «進去» «、» «讓» he «可以» «來得» «及» «扣款» then/just good
  4. (12%) «報稅» «扣款» fairly no/not «開始» «，» I «只是» «先» «把» money «放» «進去» «、» «讓» he «可以» «來得» «及» «扣款» then/just good
  5. (12%) «報稅» «扣款» still no/not «開始» «，» I «只是» «先» «把» money «放» «進去» «、» «讓» he «可以» «來得» «及» «扣款» exactly good
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/2 7:57 PM]
**Chinese:** 老闆娘帶我過來放錢的等等，我們就回他們家了
**Primary (H=2.32):** «老» «闆» «娘» bring I come «放» money «，» we then/just return/go back they «家» [completed]
**Alternatives:**
  1. (13%) «老» «闆» «娘» bring I come «放» money «，» we then/just return/go back they «家» [completed]
  2. (13%) «老» «闆» «娘» wear I come «放» money «，» we then/just return/go back they «家» [completed]
  3. (13%) «老» «闆» «娘» lead/guide I come «放» money «，» we then/just return/go back they «家» [completed]
  4. (13%) «老» «闆» «娘» bring I come «放» money «，» we exactly return/go back they «家» [completed]
  5. (13%) «老» «闆» «娘» bring I come «放» money «，» we as_soon_as return/go back they «家» [completed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/4 10:34 AM]
**Chinese:** 吃早餐了
**Primary (H=2.30):** [I, 36%] eat breakfast [completed]
**Alternatives:**
  1. (22%) [I, 36%] eat breakfast [completed]
  2. (21%) [you, 36%] eat breakfast [completed]
  3. (20%) [I, 36%] eat breakfast [now/changed]
  4. (20%) [I, 36%] eat breakfast (too much)
  5. (13%) [we, 22%] eat breakfast [completed]
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly

### [3/4 6:13 PM]
**Chinese:** 那這個針灸不錯，改天就可以再去
**Primary (H=2.00):** «那» «這個» «針灸» «不錯» «，» «改天» then/just «可以» «再» go
**Alternatives:**
  1. (25%) «那» «這個» «針灸» «不錯» «，» «改天» then/just «可以» «再» go
  2. (25%) «那» «這個» «針灸» «不錯» «，» «改天» exactly «可以» «再» go
  3. (25%) «那» «這個» «針灸» «不錯» «，» «改天» as_soon_as «可以» «再» go
  4. (25%) «那» «這個» «針灸» «不錯» «，» «改天» only «可以» «再» go
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/4 9:00 PM]
**Chinese:** 快去吃晚餐太晚了
**Primary (H=2.30):** [you, 37%] «快» go eat dinner «太晚» [completed]
**Alternatives:**
  1. (22%) [you, 37%] «快» go eat dinner «太晚» [completed]
  2. (21%) [I, 36%] «快» go eat dinner «太晚» [completed]
  3. (20%) [you, 37%] «快» go eat dinner «太晚» [now/changed]
  4. (20%) [you, 37%] «快» go eat dinner «太晚» (too much)
  5. (13%) [we, 21%] «快» go eat dinner «太晚» [completed]
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly

### [3/6 12:21 PM]
**Chinese:** 快去補睡吧
**Primary (H=2.32):** [you, 37%] «快» go «補» «睡» (let's / how about)
**Alternatives:**
  1. (18%) [you, 37%] «快» go «補» «睡» (let's / how about)
  2. (17%) [you, 37%] «快» go «補» «睡» (fine / I suppose)
  3. (17%) [you, 37%] «快» go «補» «睡» (I think / probably)
  4. (17%) [you, 37%] «快» go «補» «睡» (you should)
  5. (17%) [I, 36%] «快» go «補» «睡» (let's / how about)
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **吧**: suggestion: Let's... / How about..., concession: Fine, go ahead / I suppose so, uncertainty: I think so / probably, softened_command: You should... (softened)

### [3/6 2:49 PM]
**Chinese:** 沒關係，改天我再紐約公司負責、你就在外州這裡負責
**Primary (H=2.32):** [you, 37%] no/not «關» «係» «，» «改天» I «再» New York company «負責» «、» you then/just «在外» «州» «這裡» «負責»
**Alternatives:**
  1. (17%) [you, 37%] no/not «關» «係» «，» «改天» I «再» New York company «負責» «、» you then/just «在外» «州» «這裡» «負責»
  2. (17%) [you, 37%] no/not «關» «係» «，» «改天» I «再» New York company «負責» «、» you exactly «在外» «州» «這裡» «負責»
  3. (17%) [you, 37%] no/not «關» «係» «，» «改天» I «再» New York company «負責» «、» you as_soon_as «在外» «州» «這裡» «負責»
  4. (17%) [you, 37%] no/not «關» «係» «，» «改天» I «再» New York company «負責» «、» you only «在外» «州» «這裡» «負責»
  5. (17%) [I, 36%] no/not «關» «係» «，» «改天» I «再» New York company «負責» «、» you then/just «在外» «州» «這裡» «負責»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/7 8:49 AM]
**Chinese:** 我在認真打工幾個月，我到時候要在紐約開量子環產品的店才有資本
**Primary (H=2.32):** I «在» «認真» «打工» «幾個» «月» «，» I arrive «時候» «要» «在» New York open «量子» «環產品» «店» «才» have «資本»
**Alternatives:**
  1. (17%) I «在» «認真» «打工» «幾個» «月» «，» I arrive «時候» «要» «在» New York open «量子» «環產品» «店» «才» have «資本»
  2. (17%) I «在» «認真» «打工» «幾個» «月» «，» I succeed «時候» «要» «在» New York open «量子» «環產品» «店» «才» have «資本»
  3. (17%) I «在» «認真» «打工» «幾個» «月» «，» I arrive «時候» «要» «在» New York start/operate «量子» «環產品» «店» «才» have «資本»
  4. (17%) I «在» «認真» «打工» «幾個» «月» «，» I arrive «時候» «要» «在» New York drive «量子» «環產品» «店» «才» have «資本»
  5. (17%) I «在» «認真» «打工» «幾個» «月» «，» I arrive «時候» «要» «在» New York turn_on «量子» «環產品» «店» «才» have «資本»
**Ambiguities detected:**
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **開**: open: To open, start/operate: To start a business/operate, drive: To drive a vehicle, turn_on: To turn on/switch on

### [3/7 8:49 AM]
**Chinese:** 快去吃早餐吧，我們快到店了
**Primary (H=2.32):** [you, 37%] «快» go eat breakfast (let's / how about) «，» we «快» arrive «店» [completed]
**Alternatives:**
  1. (18%) [you, 37%] «快» go eat breakfast (let's / how about) «，» we «快» arrive «店» [completed]
  2. (18%) [you, 37%] «快» go eat breakfast (let's / how about) «，» we «快» succeed «店» [completed]
  3. (17%) [I, 36%] «快» go eat breakfast (let's / how about) «，» we «快» arrive «店» [completed]
  4. (17%) [you, 37%] «快» go eat breakfast (let's / how about) «，» we «快» arrive «店» [now/changed]
  5. (17%) [you, 37%] «快» go eat breakfast (let's / how about) «，» we «快» arrive «店» (too much)
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)

### [3/9 12:29 PM]
**Chinese:** 好的，開車注意安全
**Primary (H=2.00):** [I, 50%] good «，» drive «注意安全»
**Alternatives:**
  1. (34%) [I, 50%] good «，» drive «注意安全»
  2. (34%) [I, 50%] ok/agreed «，» drive «注意安全»
  3. (18%) [we, 28%] good «，» drive «注意安全»
  4. (11%) [you, 16%] good «，» drive «注意安全»
  5. (3%) [they, 4%] good «，» drive «注意安全»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/10 12:37 PM]
**Chinese:** 好的、到時候我們大家一起做生意
**Primary (H=2.21):** [I, 50%] good «、» arrive «時候» we everyone «一起» «做生意»
**Alternatives:**
  1. (25%) [I, 50%] good «、» arrive «時候» we everyone «一起» «做生意»
  2. (25%) [I, 50%] ok/agreed «、» arrive «時候» we everyone «一起» «做生意»
  3. (25%) [I, 50%] good «、» succeed «時候» we everyone «一起» «做生意»
  4. (14%) [we, 28%] good «、» arrive «時候» we everyone «一起» «做生意»
  5. (8%) [you, 16%] good «、» arrive «時候» we everyone «一起» «做生意»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)

### [3/10 7:30 PM]
**Chinese:** 方便就好、有吃比較重要
**Primary (H=2.32):** [you, 56%] «方便» then/just good «、» have eat «比較» important
**Alternatives:**
  1. (17%) [you, 56%] «方便» then/just good «、» have eat «比較» important
  2. (17%) [you, 56%] «方便» exactly good «、» have eat «比較» important
  3. (17%) [you, 56%] «方便» as_soon_as good «、» have eat «比較» important
  4. (17%) [you, 56%] «方便» only good «、» have eat «比較» important
  5. (17%) [you, 56%] «方便» then/just ok/agreed «、» have eat «比較» important
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/12 11:35 AM]
**Chinese:** 沒事、朋友之間、想說什麼就說什麼才不會過得這麼辛苦
**Primary (H=2.32):** [I, 36%] it's nothing/no problem «、» friend «之間» «、» want/think say/speak «什麼» then/just say/speak «什麼» «才» not «會» «這麼» hard/difficult
**Alternatives:**
  1. (10%) [I, 36%] it's nothing/no problem «、» friend «之間» «、» want/think say/speak «什麼» then/just say/speak «什麼» «才» not «會» «這麼» hard/difficult
  2. (10%) [I, 36%] it's nothing/no problem «、» friend «之間» «、» want/think say/speak «什麼» then/just say/speak «什麼» «才» not «會» «這麼» hard/difficult
  3. (10%) [I, 36%] it's nothing/no problem «、» friend «之間» «、» want/think say/speak «什麼» then/just say/speak «什麼» «才» not «會» «這麼» hard/difficult
  4. (10%) [I, 36%] it's nothing/no problem «、» friend «之間» «、» want/think say/speak «什麼» exactly say/speak «什麼» «才» not «會» «這麼» hard/difficult
  5. (10%) [I, 36%] it's nothing/no problem «、» friend «之間» «、» want/think say/speak «什麼» as_soon_as say/speak «什麼» «才» not «會» «這麼» hard/difficult
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to

### [3/12 11:59 AM]
**Chinese:** 沒關係，人跟人聊天本來就是開心就好
**Primary (H=2.32):** [I, 36%] no/not «關» «係» «，» «人» «跟» «人» «聊天» «本來» «就是» happy then/just good
**Alternatives:**
  1. (15%) [I, 36%] no/not «關» «係» «，» «人» «跟» «人» «聊天» «本來» «就是» happy then/just good
  2. (15%) [I, 36%] no/not «關» «係» «，» «人» «跟» «人» «聊天» «本來» «就是» happy exactly good
  3. (15%) [I, 36%] no/not «關» «係» «，» «人» «跟» «人» «聊天» «本來» «就是» happy as_soon_as good
  4. (15%) [I, 36%] no/not «關» «係» «，» «人» «跟» «人» «聊天» «本來» «就是» happy only good
  5. (15%) [I, 36%] no/not «關» «係» «，» «人» «跟» «人» «聊天» «本來» «就是» happy then/just ok/agreed
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/14 3:28 PM]
**Chinese:** 很好、林渼惠
**Primary (H=2.00):** [I, 50%] «很» good «、» «林» «渼» «惠»
**Alternatives:**
  1. (34%) [I, 50%] «很» good «、» «林» «渼» «惠»
  2. (34%) [I, 50%] «很» ok/agreed «、» «林» «渼» «惠»
  3. (18%) [we, 28%] «很» good «、» «林» «渼» «惠»
  4. (11%) [you, 16%] «很» good «、» «林» «渼» «惠»
  5. (3%) [they, 4%] «很» good «、» «林» «渼» «惠»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/15 10:22 AM]
**Chinese:** 這一對夫妻前兩天就預約了
**Primary (H=2.32):** «這» «一對» «夫妻» «前» «兩天» then/just «預約» [completed]
**Alternatives:**
  1. (17%) «這» «一對» «夫妻» «前» «兩天» then/just «預約» [completed]
  2. (17%) «這» «一對» «夫妻» «前» «兩天» exactly «預約» [completed]
  3. (17%) «這» «一對» «夫妻» «前» «兩天» as_soon_as «預約» [completed]
  4. (17%) «這» «一對» «夫妻» «前» «兩天» only «預約» [completed]
  5. (16%) «這» «一對» «夫妻» «前» «兩天» then/just «預約» [now/changed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/15 1:52 PM]
**Chinese:** 很好加油
**Primary (H=2.12):** [I, 36%] «很» good keep it up/go for it
**Alternatives:**
  1. (27%) [I, 36%] «很» good keep it up/go for it
  2. (27%) [I, 36%] «很» ok/agreed keep it up/go for it
  3. (26%) [you, 36%] «很» good keep it up/go for it
  4. (16%) [we, 22%] «很» good keep it up/go for it
  5. (3%) [they, 5%] «很» good keep it up/go for it
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/16 11:34 AM]
**Chinese:** 你有看過這個是什麼水果嗎？
**Primary (H=2.32):** you have look/see «這個» is/am/are «什麼» «水果» «？»
**Alternatives:**
  1. (17%) you have look/see «這個» is/am/are «什麼» «水果» «？»
  2. (17%) you have read «這個» is/am/are «什麼» «水果» «？»
  3. (17%) you have visit «這個» is/am/are «什麼» «水果» «？»
  4. (17%) you have think/consider «這個» is/am/are «什麼» «水果» «？»
  5. (17%) you have watch «這個» is/am/are «什麼» «水果» «？»
**Ambiguities detected:**
  - particle on **嗎**: yes_no_question: Is it? / Did you?, rhetorical: Isn't it obvious?
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [3/16 11:34 AM]
**Chinese:** 我們台灣沒看過
**Primary (H=2.32):** we Taiwan no/not look/see
**Alternatives:**
  1. (20%) we Taiwan no/not look/see
  2. (20%) we Taiwan no/not read
  3. (20%) we Taiwan no/not visit
  4. (20%) we Taiwan no/not think/consider
  5. (20%) we Taiwan no/not watch
**Ambiguities detected:**
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [3/17 12:06 PM]
**Chinese:** 目前我來美國、都還沒有時間出去玩
**Primary (H=2.00):** «目前» I come «美國» «、» «都» still don't have time «出去玩»
**Alternatives:**
  1. (25%) «目前» I come «美國» «、» «都» still don't have time «出去玩»
  2. (25%) «目前» I come «美國» «、» «都» also don't have time «出去玩»
  3. (25%) «目前» I come «美國» «、» «都» even don't have time «出去玩»
  4. (25%) «目前» I come «美國» «、» «都» fairly don't have time «出去玩»
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/19 10:56 AM]
**Chinese:** 迎接好的運氣
**Primary (H=2.12):** [I, 36%] «迎接» good «運氣»
**Alternatives:**
  1. (27%) [I, 36%] «迎接» good «運氣»
  2. (27%) [I, 36%] «迎接» ok/agreed «運氣»
  3. (26%) [you, 36%] «迎接» good «運氣»
  4. (16%) [we, 22%] «迎接» good «運氣»
  5. (3%) [they, 5%] «迎接» good «運氣»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/19 10:56 AM]
**Chinese:** 明天、找時間拿剪刀、修一點點頭髮、壞運去、再來就一整年都是好運氣
**Primary (H=2.32):** [I, 36%] tomorrow «、» «找» time «拿» «剪刀» «、» «修» «一點點» «頭» «髮» «、» «壞» «運去» «、» «再來» then/just «一» «整年» «都» is/am/are good «運氣»
**Alternatives:**
  1. (15%) [I, 36%] tomorrow «、» «找» time «拿» «剪刀» «、» «修» «一點點» «頭» «髮» «、» «壞» «運去» «、» «再來» then/just «一» «整年» «都» is/am/are good «運氣»
  2. (15%) [I, 36%] tomorrow «、» «找» time «拿» «剪刀» «、» «修» «一點點» «頭» «髮» «、» «壞» «運去» «、» «再來» exactly «一» «整年» «都» is/am/are good «運氣»
  3. (15%) [I, 36%] tomorrow «、» «找» time «拿» «剪刀» «、» «修» «一點點» «頭» «髮» «、» «壞» «運去» «、» «再來» as_soon_as «一» «整年» «都» is/am/are good «運氣»
  4. (15%) [I, 36%] tomorrow «、» «找» time «拿» «剪刀» «、» «修» «一點點» «頭» «髮» «、» «壞» «運去» «、» «再來» only «一» «整年» «都» is/am/are good «運氣»
  5. (15%) [I, 36%] tomorrow «、» «找» time «拿» «剪刀» «、» «修» «一點點» «頭» «髮» «、» «壞» «運去» «、» «再來» then/just «一» «整年» «都» is/am/are ok/agreed «運氣»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/19 11:15 AM]
**Chinese:** 你說你揮霍無度、錢還在成長、有這麼好的投資
**Primary (H=2.32):** you say/speak you «揮霍» «無度» «、» money still «在» «成長» «、» have «這麼» good «投資»
**Alternatives:**
  1. (14%) you say/speak you «揮霍» «無度» «、» money still «在» «成長» «、» have «這麼» good «投資»
  2. (14%) you scold you «揮霍» «無度» «、» money still «在» «成長» «、» have «這麼» good «投資»
  3. (14%) you mean you «揮霍» «無度» «、» money still «在» «成長» «、» have «這麼» good «投資»
  4. (14%) you say/speak you «揮霍» «無度» «、» money also «在» «成長» «、» have «這麼» good «投資»
  5. (14%) you say/speak you «揮霍» «無度» «、» money even «在» «成長» «、» have «這麼» good «投資»
**Ambiguities detected:**
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/19 11:27 AM]
**Chinese:** 20,000美元留起來、不要亂投資，每個月慢慢存1000、到時候我們纽约要開店、你可以過來參考、從中幫忙賺錢
**Primary (H=2.32):** [you, 56%] «20» «,» «000» «美元» «留起» come «、» «不要» «亂» «投資» «，» «每個» «月» slowly/take your time save «1000» «、» arrive «時候» we «纽约» «要» open «店» «、» you «可以» «過來» «參考» «、» «從» «中» help busy «賺» money
**Alternatives:**
  1. (15%) [you, 56%] «20» «,» «000» «美元» «留起» come «、» «不要» «亂» «投資» «，» «每個» «月» slowly/take your time save «1000» «、» arrive «時候» we «纽约» «要» open «店» «、» you «可以» «過來» «參考» «、» «從» «中» help busy «賺» money
  2. (15%) [you, 56%] «20» «,» «000» «美元» «留起» come «、» «不要» «亂» «投資» «，» «每個» «月» slowly/take your time save «1000» «、» succeed «時候» we «纽约» «要» open «店» «、» you «可以» «過來» «參考» «、» «從» «中» help busy «賺» money
  3. (15%) [you, 56%] «20» «,» «000» «美元» «留起» come «、» «不要» «亂» «投資» «，» «每個» «月» slowly/take your time save «1000» «、» arrive «時候» we «纽约» «要» start/operate «店» «、» you «可以» «過來» «參考» «、» «從» «中» help busy «賺» money
  4. (15%) [you, 56%] «20» «,» «000» «美元» «留起» come «、» «不要» «亂» «投資» «，» «每個» «月» slowly/take your time save «1000» «、» arrive «時候» we «纽约» «要» drive «店» «、» you «可以» «過來» «參考» «、» «從» «中» help busy «賺» money
  5. (15%) [you, 56%] «20» «,» «000» «美元» «留起» come «、» «不要» «亂» «投資» «，» «每個» «月» slowly/take your time save «1000» «、» arrive «時候» we «纽约» «要» turn_on «店» «、» you «可以» «過來» «參考» «、» «從» «中» help busy «賺» money
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **開**: open: To open, start/operate: To start a business/operate, drive: To drive a vehicle, turn_on: To turn on/switch on

### [3/19 11:27 AM]
**Chinese:** 到時候你才有本錢、可以進行一點點的投資、不要一次性拿太多、大家一起做比較沒風險、大家平分、積少成多、慢慢累積財富
**Primary (H=2.26):** [you, 56%] arrive «時候» you «才» have «本» money «、» «可以» «進行» «一點點» «投資» «、» «不要» «一次性» «拿» «太» «多» «、» everyone «一起» do/make «比較» no/not «風險» «、» everyone «平分» «、» «積少» «成» «多» «、» slowly/take your time «累積» «財富»
**Alternatives:**
  1. (21%) [you, 56%] arrive «時候» you «才» have «本» money «、» «可以» «進行» «一點點» «投資» «、» «不要» «一次性» «拿» «太» «多» «、» everyone «一起» do/make «比較» no/not «風險» «、» everyone «平分» «、» «積少» «成» «多» «、» slowly/take your time «累積» «財富»
  2. (21%) [you, 56%] succeed «時候» you «才» have «本» money «、» «可以» «進行» «一點點» «投資» «、» «不要» «一次性» «拿» «太» «多» «、» everyone «一起» do/make «比較» no/not «風險» «、» everyone «平分» «、» «積少» «成» «多» «、» slowly/take your time «累積» «財富»
  3. (21%) [you, 56%] arrive «時候» you «才» have «本» money «、» «可以» «進行» «一點點» «投資» «、» «不要» «一次性» «拿» «太» «多» «、» everyone «一起» work_as «比較» no/not «風險» «、» everyone «平分» «、» «積少» «成» «多» «、» slowly/take your time «累積» «財富»
  4. (21%) [you, 56%] arrive «時候» you «才» have «本» money «、» «可以» «進行» «一點點» «投資» «、» «不要» «一次性» «拿» «太» «多» «、» everyone «一起» conduct «比較» no/not «風險» «、» everyone «平分» «、» «積少» «成» «多» «、» slowly/take your time «累積» «財富»
  5. (8%) [I, 22%] arrive «時候» you «才» have «本» money «、» «可以» «進行» «一點點» «投資» «、» «不要» «一次性» «拿» «太» «多» «、» everyone «一起» do/make «比較» no/not «風險» «、» everyone «平分» «、» «積少» «成» «多» «、» slowly/take your time «累積» «財富»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)

### [3/19 12:00 PM]
**Chinese:** 聽說你們這裡的人、很少有存款的、你是少部分的優秀人士、會存款是好事、以備不時需要
**Primary (H=2.17):** [you, 56%] «聽» say/speak you all «這裡» «人» «、» «很少» have «存款» «、» you is/am/are «少部分» «優秀» «人士» «、» «會» «存款» is/am/are «好事» «、» «以備» «不時» «需要»
**Alternatives:**
  1. (26%) [you, 56%] «聽» say/speak you all «這裡» «人» «、» «很少» have «存款» «、» you is/am/are «少部分» «優秀» «人士» «、» «會» «存款» is/am/are «好事» «、» «以備» «不時» «需要»
  2. (26%) [you, 56%] «聽» scold you all «這裡» «人» «、» «很少» have «存款» «、» you is/am/are «少部分» «優秀» «人士» «、» «會» «存款» is/am/are «好事» «、» «以備» «不時» «需要»
  3. (26%) [you, 56%] «聽» mean you all «這裡» «人» «、» «很少» have «存款» «、» you is/am/are «少部分» «優秀» «人士» «、» «會» «存款» is/am/are «好事» «、» «以備» «不時» «需要»
  4. (10%) [I, 22%] «聽» say/speak you all «這裡» «人» «、» «很少» have «存款» «、» you is/am/are «少部分» «優秀» «人士» «、» «會» «存款» is/am/are «好事» «、» «以備» «不時» «需要»
  5. (8%) [we, 17%] «聽» say/speak you all «這裡» «人» «、» «很少» have «存款» «、» you is/am/are «少部分» «優秀» «人士» «、» «會» «存款» is/am/are «好事» «、» «以備» «不時» «需要»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to

### [3/19 12:21 PM]
**Chinese:** 你說說、你幾年、幾月、幾日生、你的要求是幾歲的女孩我來幫你找、讓你有個女朋友、我會幫你找我紐約好朋友裡面的女孩其中一個、讓你們兩個互相認識互相聊天、不喜歡再換人、這樣你才可以、不要浪費時間、
**Primary (H=2.32):** you say/speak say/speak «、» you «幾年» «、» «幾月» «、» «幾日» «生» «、» you «要求» is/am/are «幾歲» «女孩» I come help you «找» «、» «讓» you «有個» «女朋友» «、» I «會» help you «找» «我紐» «約» good friend «裡面» «女孩» «其中» «一個» «、» «讓» you all «兩個» «互相» know/meet «互相» «聊天» «、» not like «再» «換» «人» «、» «這樣» you «才» «可以» «、» «不要» «浪費» time «、»
**Alternatives:**
  1. (17%) you say/speak say/speak «、» you «幾年» «、» «幾月» «、» «幾日» «生» «、» you «要求» is/am/are «幾歲» «女孩» I come help you «找» «、» «讓» you «有個» «女朋友» «、» I «會» help you «找» «我紐» «約» good friend «裡面» «女孩» «其中» «一個» «、» «讓» you all «兩個» «互相» know/meet «互相» «聊天» «、» not like «再» «換» «人» «、» «這樣» you «才» «可以» «、» «不要» «浪費» time «、»
  2. (17%) you say/speak say/speak «、» you «幾年» «、» «幾月» «、» «幾日» «生» «、» you «要求» is/am/are «幾歲» «女孩» I come help you «找» «、» «讓» you «有個» «女朋友» «、» I «會» help you «找» «我紐» «約» good friend «裡面» «女孩» «其中» «一個» «、» «讓» you all «兩個» «互相» know/meet «互相» «聊天» «、» not like «再» «換» «人» «、» «這樣» you «才» «可以» «、» «不要» «浪費» time «、»
  3. (17%) you say/speak say/speak «、» you «幾年» «、» «幾月» «、» «幾日» «生» «、» you «要求» is/am/are «幾歲» «女孩» I come help you «找» «、» «讓» you «有個» «女朋友» «、» I «會» help you «找» «我紐» «約» good friend «裡面» «女孩» «其中» «一個» «、» «讓» you all «兩個» «互相» know/meet «互相» «聊天» «、» not like «再» «換» «人» «、» «這樣» you «才» «可以» «、» «不要» «浪費» time «、»
  4. (17%) you scold scold «、» you «幾年» «、» «幾月» «、» «幾日» «生» «、» you «要求» is/am/are «幾歲» «女孩» I come help you «找» «、» «讓» you «有個» «女朋友» «、» I «會» help you «找» «我紐» «約» good friend «裡面» «女孩» «其中» «一個» «、» «讓» you all «兩個» «互相» know/meet «互相» «聊天» «、» not like «再» «換» «人» «、» «這樣» you «才» «可以» «、» «不要» «浪費» time «、»
  5. (17%) you mean mean «、» you «幾年» «、» «幾月» «、» «幾日» «生» «、» you «要求» is/am/are «幾歲» «女孩» I come help you «找» «、» «讓» you «有個» «女朋友» «、» I «會» help you «找» «我紐» «約» good friend «裡面» «女孩» «其中» «一個» «、» «讓» you all «兩個» «互相» know/meet «互相» «聊天» «、» not like «再» «換» «人» «、» «這樣» you «才» «可以» «、» «不要» «浪費» time «、»
**Ambiguities detected:**
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/19 5:31 PM]
**Chinese:** 這個是華人開的、還是你們美國人開的
**Primary (H=2.32):** «這個» is/am/are «華» «人» open «、» «還是» you all «美國» «人» open
**Alternatives:**
  1. (11%) «這個» is/am/are «華» «人» open «、» «還是» you all «美國» «人» open
  2. (11%) «這個» is/am/are «華» «人» open «、» «還是» you all «美國» «人» open
  3. (11%) «這個» is/am/are «華» «人» open «、» «還是» you all «美國» «人» open
  4. (11%) «這個» is/am/are «華» «人» open «、» «還是» you all «美國» «人» open
  5. (11%) «這個» is/am/are «華» «人» open «、» «還是» you all «美國» «人» open
**Ambiguities detected:**
  - polysemy on **開**: open: To open, start/operate: To start a business/operate, drive: To drive a vehicle, turn_on: To turn on/switch on
  - polysemy on **開**: open: To open, start/operate: To start a business/operate, drive: To drive a vehicle, turn_on: To turn on/switch on

### [3/20 9:40 AM]
**Chinese:** 吃早餐了
**Primary (H=2.30):** [I, 36%] eat breakfast [completed]
**Alternatives:**
  1. (22%) [I, 36%] eat breakfast [completed]
  2. (21%) [you, 36%] eat breakfast [completed]
  3. (20%) [I, 36%] eat breakfast [now/changed]
  4. (20%) [I, 36%] eat breakfast (too much)
  5. (13%) [we, 22%] eat breakfast [completed]
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly

### [3/20 9:40 AM]
**Chinese:** 起床就剪好了
**Primary (H=2.32):** [I, 36%] wake up then/just «剪» good [completed]
**Alternatives:**
  1. (12%) [I, 36%] wake up then/just «剪» good [completed]
  2. (12%) [I, 36%] wake up exactly «剪» good [completed]
  3. (12%) [I, 36%] wake up as_soon_as «剪» good [completed]
  4. (12%) [I, 36%] wake up only «剪» good [completed]
  5. (12%) [I, 36%] wake up then/just «剪» ok/agreed [completed]
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/20 2:23 PM]
**Chinese:** 所以不用太忌諱、想聊什麼就聊什麼
**Primary (H=2.32):** [I, 36%] «所以» «不用» «太» «忌諱» «、» want/think «聊» «什麼» then/just «聊» «什麼»
**Alternatives:**
  1. (17%) [I, 36%] «所以» «不用» «太» «忌諱» «、» want/think «聊» «什麼» then/just «聊» «什麼»
  2. (17%) [I, 36%] «所以» «不用» «太» «忌諱» «、» want/think «聊» «什麼» exactly «聊» «什麼»
  3. (17%) [I, 36%] «所以» «不用» «太» «忌諱» «、» want/think «聊» «什麼» as_soon_as «聊» «什麼»
  4. (17%) [I, 36%] «所以» «不用» «太» «忌諱» «、» want/think «聊» «什麼» only «聊» «什麼»
  5. (17%) [you, 36%] «所以» «不用» «太» «忌諱» «、» want/think «聊» «什麼» then/just «聊» «什麼»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/20 4:57 PM]
**Chinese:** 這樣子看起來很有精神、今天剪頭髮最好了，一年當中每年的農曆2月2號剪頭髮最好
**Primary (H=2.32):** «這樣» «子» look/see «起來» «很» have «精神» «、» today «剪» «頭» «髮» «最好» [completed] «，» «一年» «當中» «每年» «農» «曆» «2» «月» «2» «號» «剪» «頭» «髮» «最好»
**Alternatives:**
  1. (20%) «這樣» «子» look/see «起來» «很» have «精神» «、» today «剪» «頭» «髮» «最好» [completed] «，» «一年» «當中» «每年» «農» «曆» «2» «月» «2» «號» «剪» «頭» «髮» «最好»
  2. (20%) «這樣» «子» read «起來» «很» have «精神» «、» today «剪» «頭» «髮» «最好» [completed] «，» «一年» «當中» «每年» «農» «曆» «2» «月» «2» «號» «剪» «頭» «髮» «最好»
  3. (20%) «這樣» «子» visit «起來» «很» have «精神» «、» today «剪» «頭» «髮» «最好» [completed] «，» «一年» «當中» «每年» «農» «曆» «2» «月» «2» «號» «剪» «頭» «髮» «最好»
  4. (20%) «這樣» «子» think/consider «起來» «很» have «精神» «、» today «剪» «頭» «髮» «最好» [completed] «，» «一年» «當中» «每年» «農» «曆» «2» «月» «2» «號» «剪» «頭» «髮» «最好»
  5. (20%) «這樣» «子» watch «起來» «很» have «精神» «、» today «剪» «頭» «髮» «最好» [completed] «，» «一年» «當中» «每年» «農» «曆» «2» «月» «2» «號» «剪» «頭» «髮» «最好»
**Ambiguities detected:**
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [3/20 4:57 PM]
**Chinese:** 我說今天天氣很好、前幾天從老闆娘他們家過來店裡拍的
**Primary (H=2.00):** I say/speak today «天氣» «很» good «、» «前» «幾天» «從» «老» «闆» «娘» he «們» «家» come «店» «裡» «拍»
**Alternatives:**
  1. (25%) I say/speak today «天氣» «很» good «、» «前» «幾天» «從» «老» «闆» «娘» he «們» «家» come «店» «裡» «拍»
  2. (25%) I scold today «天氣» «很» good «、» «前» «幾天» «從» «老» «闆» «娘» he «們» «家» come «店» «裡» «拍»
  3. (25%) I mean today «天氣» «很» good «、» «前» «幾天» «從» «老» «闆» «娘» he «們» «家» come «店» «裡» «拍»
  4. (25%) I say/speak today «天氣» «很» ok/agreed «、» «前» «幾天» «從» «老» «闆» «娘» he «們» «家» come «店» «裡» «拍»
**Ambiguities detected:**
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/20 4:57 PM]
**Chinese:** 拍照隨性開心就好、我很少拍照，因為我不喜歡拍照
**Primary (H=2.32):** [I, 36%] «拍照» «隨性» happy then/just good «、» I «很少» «拍照» «，» «因為» I not like «拍照»
**Alternatives:**
  1. (15%) [I, 36%] «拍照» «隨性» happy then/just good «、» I «很少» «拍照» «，» «因為» I not like «拍照»
  2. (15%) [I, 36%] «拍照» «隨性» happy exactly good «、» I «很少» «拍照» «，» «因為» I not like «拍照»
  3. (15%) [I, 36%] «拍照» «隨性» happy as_soon_as good «、» I «很少» «拍照» «，» «因為» I not like «拍照»
  4. (15%) [I, 36%] «拍照» «隨性» happy only good «、» I «很少» «拍照» «，» «因為» I not like «拍照»
  5. (15%) [I, 36%] «拍照» «隨性» happy then/just ok/agreed «、» I «很少» «拍照» «，» «因為» I not like «拍照»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/20 8:37 PM]
**Chinese:** 麵條煮好了，撈起來、再燙豆腐
**Primary (H=2.12):** [I, 36%] «麵» «條» cook good [completed] «，» «撈» «起來» «、» «再» «燙» «豆腐»
**Alternatives:**
  1. (27%) [I, 36%] «麵» «條» cook good [completed] «，» «撈» «起來» «、» «再» «燙» «豆腐»
  2. (27%) [I, 36%] «麵» «條» cook ok/agreed [completed] «，» «撈» «起來» «、» «再» «燙» «豆腐»
  3. (26%) [you, 36%] «麵» «條» cook good [completed] «，» «撈» «起來» «、» «再» «燙» «豆腐»
  4. (16%) [we, 22%] «麵» «條» cook good [completed] «，» «撈» «起來» «、» «再» «燙» «豆腐»
  5. (3%) [they, 5%] «麵» «條» cook good [completed] «，» «撈» «起來» «、» «再» «燙» «豆腐»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/20 8:37 PM]
**Chinese:** 好吃就好
**Primary (H=2.32):** [I, 36%] «好吃» then/just good
**Alternatives:**
  1. (15%) [I, 36%] «好吃» then/just good
  2. (15%) [I, 36%] «好吃» exactly good
  3. (15%) [I, 36%] «好吃» as_soon_as good
  4. (15%) [I, 36%] «好吃» only good
  5. (15%) [I, 36%] «好吃» then/just ok/agreed
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/20 8:37 PM]
**Chinese:** 怎麼比我們纽约還貴？
**Primary (H=2.00):** «怎麼» «比» we «纽约» still expensive «？»
**Alternatives:**
  1. (25%) «怎麼» «比» we «纽约» still expensive «？»
  2. (25%) «怎麼» «比» we «纽约» also expensive «？»
  3. (25%) «怎麼» «比» we «纽约» even expensive «？»
  4. (25%) «怎麼» «比» we «纽约» fairly expensive «？»
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/20 8:37 PM]
**Chinese:** 這是我們台灣的茶壺跟茶組、還有台灣的茶葉
**Primary (H=2.00):** «這» is/am/are we Taiwan «茶壺» «跟» «茶» «組» «、» still have Taiwan «茶葉»
**Alternatives:**
  1. (25%) «這» is/am/are we Taiwan «茶壺» «跟» «茶» «組» «、» still have Taiwan «茶葉»
  2. (25%) «這» is/am/are we Taiwan «茶壺» «跟» «茶» «組» «、» also have Taiwan «茶葉»
  3. (25%) «這» is/am/are we Taiwan «茶壺» «跟» «茶» «組» «、» even have Taiwan «茶葉»
  4. (25%) «這» is/am/are we Taiwan «茶壺» «跟» «茶» «組» «、» fairly have Taiwan «茶葉»
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/20 8:37 PM]
**Chinese:** 我的所有朋友都說我住這裡太貴了、我們兩個女生住三個房間太浪費了、每個月包含房租一大堆的家加起來就3000
**Primary (H=2.32):** I «所有» friend «都» say/speak I live «這裡» «太» expensive [completed] «、» we «兩個» «女生» live «三個» «房間» «太» «浪費» [completed] «、» «每個» «月» «包含» rent «一大堆» «家» «加起» come then/just «3000»
**Alternatives:**
  1. (17%) I «所有» friend «都» say/speak I live «這裡» «太» expensive [completed] «、» we «兩個» «女生» live «三個» «房間» «太» «浪費» [completed] «、» «每個» «月» «包含» rent «一大堆» «家» «加起» come then/just «3000»
  2. (17%) I «所有» friend «都» scold I live «這裡» «太» expensive [completed] «、» we «兩個» «女生» live «三個» «房間» «太» «浪費» [completed] «、» «每個» «月» «包含» rent «一大堆» «家» «加起» come then/just «3000»
  3. (17%) I «所有» friend «都» mean I live «這裡» «太» expensive [completed] «、» we «兩個» «女生» live «三個» «房間» «太» «浪費» [completed] «、» «每個» «月» «包含» rent «一大堆» «家» «加起» come then/just «3000»
  4. (17%) I «所有» friend «都» say/speak I live «這裡» «太» expensive [completed] «、» we «兩個» «女生» live «三個» «房間» «太» «浪費» [completed] «、» «每個» «月» «包含» rent «一大堆» «家» «加起» come exactly «3000»
  5. (17%) I «所有» friend «都» say/speak I live «這裡» «太» expensive [completed] «、» we «兩個» «女生» live «三個» «房間» «太» «浪費» [completed] «、» «每個» «月» «包含» rent «一大堆» «家» «加起» come as_soon_as «3000»
**Ambiguities detected:**
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/20 8:37 PM]
**Chinese:** 下個月我會搬去跟另外的姐姐他們大家住、聽說那裡有四個房間我還沒去過
**Primary (H=2.32):** «下個月» I «會» «搬去» «跟» «另外» «姐姐» they everyone live «、» «聽» say/speak «那裡» have «四個» «房間» I still no/not «去過»
**Alternatives:**
  1. (17%) «下個月» I «會» «搬去» «跟» «另外» «姐姐» they everyone live «、» «聽» say/speak «那裡» have «四個» «房間» I still no/not «去過»
  2. (17%) «下個月» I «會» «搬去» «跟» «另外» «姐姐» they everyone live «、» «聽» scold «那裡» have «四個» «房間» I still no/not «去過»
  3. (17%) «下個月» I «會» «搬去» «跟» «另外» «姐姐» they everyone live «、» «聽» mean «那裡» have «四個» «房間» I still no/not «去過»
  4. (17%) «下個月» I «會» «搬去» «跟» «另外» «姐姐» they everyone live «、» «聽» say/speak «那裡» have «四個» «房間» I also no/not «去過»
  5. (17%) «下個月» I «會» «搬去» «跟» «另外» «姐姐» they everyone live «、» «聽» say/speak «那裡» have «四個» «房間» I even no/not «去過»
**Ambiguities detected:**
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/20 8:37 PM]
**Chinese:** 你一個人住房租就4200、這樣子每個月工作的薪水都不夠付房租了
**Primary (H=2.32):** you «一個» «人» live rent then/just «4200» «、» «這樣» «子» «每個» «月» work salary «都» «不夠» «付» rent [completed]
**Alternatives:**
  1. (17%) you «一個» «人» live rent then/just «4200» «、» «這樣» «子» «每個» «月» work salary «都» «不夠» «付» rent [completed]
  2. (17%) you «一個» «人» live rent exactly «4200» «、» «這樣» «子» «每個» «月» work salary «都» «不夠» «付» rent [completed]
  3. (17%) you «一個» «人» live rent as_soon_as «4200» «、» «這樣» «子» «每個» «月» work salary «都» «不夠» «付» rent [completed]
  4. (17%) you «一個» «人» live rent only «4200» «、» «這樣» «子» «每個» «月» work salary «都» «不夠» «付» rent [completed]
  5. (16%) you «一個» «人» live rent then/just «4200» «、» «這樣» «子» «每個» «月» work salary «都» «不夠» «付» rent [now/changed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/20 8:37 PM]
**Chinese:** 我們兩個人$3000、平均一人一個月付1500還可以
**Primary (H=2.00):** we «兩個» «人» «$» «3000» «、» «平均» «一» «人» «一個» «月» «付» «1500» still «可以»
**Alternatives:**
  1. (25%) we «兩個» «人» «$» «3000» «、» «平均» «一» «人» «一個» «月» «付» «1500» still «可以»
  2. (25%) we «兩個» «人» «$» «3000» «、» «平均» «一» «人» «一個» «月» «付» «1500» also «可以»
  3. (25%) we «兩個» «人» «$» «3000» «、» «平均» «一» «人» «一個» «月» «付» «1500» even «可以»
  4. (25%) we «兩個» «人» «$» «3000» «、» «平均» «一» «人» «一個» «月» «付» «1500» fairly «可以»
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/20 8:37 PM]
**Chinese:** 所以我下個月要搬家的時候、我的房間裡的床、還有客廳的沙發餐桌電視、到時候都要請搬家公司搬、因為我們那時候租房子裡面全部都是空的全部都是我們兩個自己買的
**Primary (H=2.32):** «所以» I «下» «個» «月» «要» «搬家» «時候» «、» I «房間» «裡» «床» «、» still have «客廳» «沙發» «餐桌» «電視» «、» arrive «時候» «都» «要» «請» «搬家» company move «、» «因為» we «那時候» «租房子» «裡面» «全部都是» «空» «全部都是» we «兩個» oneself buy
**Alternatives:**
  1. (20%) «所以» I «下» «個» «月» «要» «搬家» «時候» «、» I «房間» «裡» «床» «、» still have «客廳» «沙發» «餐桌» «電視» «、» arrive «時候» «都» «要» «請» «搬家» company move «、» «因為» we «那時候» «租房子» «裡面» «全部都是» «空» «全部都是» we «兩個» oneself buy
  2. (20%) «所以» I «下» «個» «月» «要» «搬家» «時候» «、» I «房間» «裡» «床» «、» also have «客廳» «沙發» «餐桌» «電視» «、» arrive «時候» «都» «要» «請» «搬家» company move «、» «因為» we «那時候» «租房子» «裡面» «全部都是» «空» «全部都是» we «兩個» oneself buy
  3. (20%) «所以» I «下» «個» «月» «要» «搬家» «時候» «、» I «房間» «裡» «床» «、» even have «客廳» «沙發» «餐桌» «電視» «、» arrive «時候» «都» «要» «請» «搬家» company move «、» «因為» we «那時候» «租房子» «裡面» «全部都是» «空» «全部都是» we «兩個» oneself buy
  4. (20%) «所以» I «下» «個» «月» «要» «搬家» «時候» «、» I «房間» «裡» «床» «、» fairly have «客廳» «沙發» «餐桌» «電視» «、» arrive «時候» «都» «要» «請» «搬家» company move «、» «因為» we «那時候» «租房子» «裡面» «全部都是» «空» «全部都是» we «兩個» oneself buy
  5. (20%) «所以» I «下» «個» «月» «要» «搬家» «時候» «、» I «房間» «裡» «床» «、» still have «客廳» «沙發» «餐桌» «電視» «、» succeed «時候» «都» «要» «請» «搬家» company move «、» «因為» we «那時候» «租房子» «裡面» «全部都是» «空» «全部都是» we «兩個» oneself buy
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)

### [3/20 8:37 PM]
**Chinese:** 哇6500扣了房租4200、剩下2300還要吃一個月的費用
**Primary (H=2.26):** [you, 56%] «6500» «扣» [completed] rent «4200» «、» «剩下» «2300» still «要» eat «一個» «月» «費用»
**Alternatives:**
  1. (21%) [you, 56%] «6500» «扣» [completed] rent «4200» «、» «剩下» «2300» still «要» eat «一個» «月» «費用»
  2. (21%) [you, 56%] «6500» «扣» [completed] rent «4200» «、» «剩下» «2300» also «要» eat «一個» «月» «費用»
  3. (21%) [you, 56%] «6500» «扣» [completed] rent «4200» «、» «剩下» «2300» even «要» eat «一個» «月» «費用»
  4. (21%) [you, 56%] «6500» «扣» [completed] rent «4200» «、» «剩下» «2300» fairly «要» eat «一個» «月» «費用»
  5. (8%) [I, 22%] «6500» «扣» [completed] rent «4200» «、» «剩下» «2300» still «要» eat «一個» «月» «費用»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/20 8:37 PM]
**Chinese:** 一定可以纽约房租便宜、吃的也方便買的也方便、到時候你要是要跟我們大家一起做量子環、我們請的員工一個小時$18
**Primary (H=2.00):** «一定» «可以» «纽约» rent «便宜» «、» eat «也» «方便» buy «也» «方便» «、» arrive «時候» you «要是» «要» «跟» we everyone «一起» do/make «量子» «環» «、» we «請» «員工» «一個» «小» «時» «$» «18»
**Alternatives:**
  1. (25%) «一定» «可以» «纽约» rent «便宜» «、» eat «也» «方便» buy «也» «方便» «、» arrive «時候» you «要是» «要» «跟» we everyone «一起» do/make «量子» «環» «、» we «請» «員工» «一個» «小» «時» «$» «18»
  2. (25%) «一定» «可以» «纽约» rent «便宜» «、» eat «也» «方便» buy «也» «方便» «、» succeed «時候» you «要是» «要» «跟» we everyone «一起» do/make «量子» «環» «、» we «請» «員工» «一個» «小» «時» «$» «18»
  3. (25%) «一定» «可以» «纽约» rent «便宜» «、» eat «也» «方便» buy «也» «方便» «、» arrive «時候» you «要是» «要» «跟» we everyone «一起» work_as «量子» «環» «、» we «請» «員工» «一個» «小» «時» «$» «18»
  4. (25%) «一定» «可以» «纽约» rent «便宜» «、» eat «也» «方便» buy «也» «方便» «、» arrive «時候» you «要是» «要» «跟» we everyone «一起» conduct «量子» «環» «、» we «請» «員工» «一個» «小» «時» «$» «18»
**Ambiguities detected:**
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)

### [3/20 8:37 PM]
**Chinese:** 我到時候請的員工一個小時$18或者$20、看他們的意願要上八個小時或10個小時都可以
**Primary (H=2.32):** I arrive «時候» «請» «員工» «一個» «小» «時» «$» «18» «或者» «$» «20» «、» look/see they «意願» «要» «上» «八個» «小» «時» «或» «10» «個» «小» «時» «都» «可以»
**Alternatives:**
  1. (17%) I arrive «時候» «請» «員工» «一個» «小» «時» «$» «18» «或者» «$» «20» «、» look/see they «意願» «要» «上» «八個» «小» «時» «或» «10» «個» «小» «時» «都» «可以»
  2. (17%) I succeed «時候» «請» «員工» «一個» «小» «時» «$» «18» «或者» «$» «20» «、» look/see they «意願» «要» «上» «八個» «小» «時» «或» «10» «個» «小» «時» «都» «可以»
  3. (17%) I arrive «時候» «請» «員工» «一個» «小» «時» «$» «18» «或者» «$» «20» «、» read they «意願» «要» «上» «八個» «小» «時» «或» «10» «個» «小» «時» «都» «可以»
  4. (17%) I arrive «時候» «請» «員工» «一個» «小» «時» «$» «18» «或者» «$» «20» «、» visit they «意願» «要» «上» «八個» «小» «時» «或» «10» «個» «小» «時» «都» «可以»
  5. (17%) I arrive «時候» «請» «員工» «一個» «小» «時» «$» «18» «或者» «$» «20» «、» think/consider they «意願» «要» «上» «八個» «小» «時» «或» «10» «個» «小» «時» «都» «可以»
**Ambiguities detected:**
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [3/20 8:37 PM]
**Chinese:** 沒事，等去纽约、你先去看環境喜歡再說吧不著急
**Primary (H=2.32):** [I, 36%] it's nothing/no problem «，» go «纽约» «、» you «先» go look/see «環境» like «再» say/speak (let's / how about) not «著急»
**Alternatives:**
  1. (11%) [I, 36%] it's nothing/no problem «，» go «纽约» «、» you «先» go look/see «環境» like «再» say/speak (let's / how about) not «著急»
  2. (11%) [I, 36%] it's nothing/no problem «，» go «纽约» «、» you «先» go read «環境» like «再» say/speak (let's / how about) not «著急»
  3. (11%) [I, 36%] it's nothing/no problem «，» go «纽约» «、» you «先» go visit «環境» like «再» say/speak (let's / how about) not «著急»
  4. (11%) [I, 36%] it's nothing/no problem «，» go «纽约» «、» you «先» go think/consider «環境» like «再» say/speak (let's / how about) not «著急»
  5. (11%) [I, 36%] it's nothing/no problem «，» go «纽约» «、» you «先» go watch «環境» like «再» say/speak (let's / how about) not «著急»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to

### [3/21 11:59 AM]
**Chinese:** 我們是12點前就睡了，所以我們五六點前就會把晚餐吃完
**Primary (H=2.32):** we is/am/are «12» «點» «前» then/just «睡» [completed] «，» «所以» we «五六» «點» «前» then/just «會» «把» dinner eat «完»
**Alternatives:**
  1. (14%) we is/am/are «12» «點» «前» then/just «睡» [completed] «，» «所以» we «五六» «點» «前» then/just «會» «把» dinner eat «完»
  2. (14%) we is/am/are «12» «點» «前» then/just «睡» [completed] «，» «所以» we «五六» «點» «前» then/just «會» «把» dinner eat «完»
  3. (14%) we is/am/are «12» «點» «前» then/just «睡» [completed] «，» «所以» we «五六» «點» «前» then/just «會» «把» dinner eat «完»
  4. (14%) we is/am/are «12» «點» «前» then/just «睡» [completed] «，» «所以» we «五六» «點» «前» then/just «會» «把» dinner eat «完»
  5. (14%) we is/am/are «12» «點» «前» exactly «睡» [completed] «，» «所以» we «五六» «點» «前» exactly «會» «把» dinner eat «完»
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/21 7:32 PM]
**Chinese:** 快去吃晚餐吧
**Primary (H=2.32):** [I, 36%] «快» go eat dinner (let's / how about)
**Alternatives:**
  1. (17%) [I, 36%] «快» go eat dinner (let's / how about)
  2. (17%) [I, 36%] «快» go eat dinner (fine / I suppose)
  3. (17%) [I, 36%] «快» go eat dinner (I think / probably)
  4. (17%) [I, 36%] «快» go eat dinner (you should)
  5. (17%) [you, 36%] «快» go eat dinner (let's / how about)
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **吧**: suggestion: Let's... / How about..., concession: Fine, go ahead / I suppose so, uncertainty: I think so / probably, softened_command: You should... (softened)

### [3/21 9:09 PM]
**Chinese:** 為什麼說因果報應什麼意思啊？
**Primary (H=2.32):** «為» «什麼» say/speak «因果» «報應» «什麼» «意思» ! «？»
**Alternatives:**
  1. (17%) «為» «什麼» say/speak «因果» «報應» «什麼» «意思» ! «？»
  2. (17%) «為» «什麼» scold «因果» «報應» «什麼» «意思» ! «？»
  3. (17%) «為» «什麼» mean «因果» «報應» «什麼» «意思» ! «？»
  4. (17%) «為» «什麼» say/speak «因果» «報應» «什麼» «意思» «？»
  5. (17%) «為» «什麼» say/speak «因果» «報應» «什麼» «意思» (oh!) «？»
**Ambiguities detected:**
  - particle on **啊**: exclamation: Wow / emphasis, filler: Softening / conversational filler, realization: Oh! / I see, urging: Come on / hurry up
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to

### [3/22 1:16 PM]
**Chinese:** 早上好、我們8:30就吃早餐了、因為今天預約很多九點就開始忙了
**Primary (H=2.32):** good morning «、» we «8» «:» «30» then/just eat breakfast [completed] «、» «因為» today «預約» «很多» «九點» then/just «開始» busy [completed]
**Alternatives:**
  1. (11%) good morning «、» we «8» «:» «30» then/just eat breakfast [completed] «、» «因為» today «預約» «很多» «九點» then/just «開始» busy [completed]
  2. (11%) good morning «、» we «8» «:» «30» then/just eat breakfast [completed] «、» «因為» today «預約» «很多» «九點» then/just «開始» busy [completed]
  3. (11%) good morning «、» we «8» «:» «30» then/just eat breakfast [completed] «、» «因為» today «預約» «很多» «九點» then/just «開始» busy [completed]
  4. (11%) good morning «、» we «8» «:» «30» then/just eat breakfast [completed] «、» «因為» today «預約» «很多» «九點» then/just «開始» busy [completed]
  5. (11%) good morning «、» we «8» «:» «30» exactly eat breakfast [completed] «、» «因為» today «預約» «很多» «九點» exactly «開始» busy [completed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/22 9:02 PM]
**Chinese:** 要來吃晚餐了
**Primary (H=2.18):** [you, 56%] «要» come eat dinner [completed]
**Alternatives:**
  1. (27%) [you, 56%] «要» come eat dinner [completed]
  2. (25%) [you, 56%] «要» come eat dinner [now/changed]
  3. (25%) [you, 56%] «要» come eat dinner (too much)
  4. (11%) [I, 22%] «要» come eat dinner [completed]
  5. (8%) [we, 17%] «要» come eat dinner [completed]
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly

### [3/23 10:41 AM]
**Chinese:** 先去忙了
**Primary (H=2.30):** [I, 36%] «先去» busy [completed]
**Alternatives:**
  1. (22%) [I, 36%] «先去» busy [completed]
  2. (21%) [you, 36%] «先去» busy [completed]
  3. (20%) [I, 36%] «先去» busy [now/changed]
  4. (20%) [I, 36%] «先去» busy (too much)
  5. (13%) [we, 22%] «先去» busy [completed]
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly

### [3/23 11:02 AM]
**Chinese:** 那就學習國語
**Primary (H=2.00):** «那» then/just study/learn «國語»
**Alternatives:**
  1. (25%) «那» then/just study/learn «國語»
  2. (25%) «那» exactly study/learn «國語»
  3. (25%) «那» as_soon_as study/learn «國語»
  4. (25%) «那» only study/learn «國語»
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/24 10:23 AM]
**Chinese:** 全球吸引力、量子環是戴健康的、改善身體的所有慢性病、還有保養身體的
**Primary (H=2.00):** «全球» «吸引力» «、» «量子» «環是» wear healthy «、» improve body/health «所有» «慢性病» «、» still have «保養» body/health
**Alternatives:**
  1. (25%) «全球» «吸引力» «、» «量子» «環是» wear healthy «、» improve body/health «所有» «慢性病» «、» still have «保養» body/health
  2. (25%) «全球» «吸引力» «、» «量子» «環是» wear healthy «、» improve body/health «所有» «慢性病» «、» also have «保養» body/health
  3. (25%) «全球» «吸引力» «、» «量子» «環是» wear healthy «、» improve body/health «所有» «慢性病» «、» even have «保養» body/health
  4. (25%) «全球» «吸引力» «、» «量子» «環是» wear healthy «、» improve body/health «所有» «慢性病» «、» fairly have «保養» body/health
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/24 10:23 AM]
**Chinese:** 目前還沒想這麼多
**Primary (H=2.32):** [I, 36%] «目前» still «沒想» «這麼» «多»
**Alternatives:**
  1. (17%) [I, 36%] «目前» still «沒想» «這麼» «多»
  2. (17%) [I, 36%] «目前» also «沒想» «這麼» «多»
  3. (17%) [I, 36%] «目前» even «沒想» «這麼» «多»
  4. (17%) [I, 36%] «目前» fairly «沒想» «這麼» «多»
  5. (17%) [you, 36%] «目前» still «沒想» «這麼» «多»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/24 11:22 AM]
**Chinese:** 這四天可以到紐約跟我們碰面
**Primary (H=2.12):** [I, 36%] «這» «四天» «可以» arrive New York «跟» we «碰面»
**Alternatives:**
  1. (27%) [I, 36%] «這» «四天» «可以» arrive New York «跟» we «碰面»
  2. (27%) [I, 36%] «這» «四天» «可以» succeed New York «跟» we «碰面»
  3. (26%) [you, 36%] «這» «四天» «可以» arrive New York «跟» we «碰面»
  4. (16%) [we, 22%] «這» «四天» «可以» arrive New York «跟» we «碰面»
  5. (3%) [they, 5%] «這» «四天» «可以» arrive New York «跟» we «碰面»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)

### [3/24 11:22 AM]
**Chinese:** 那麼你就28號到法拉盛找我們
**Primary (H=2.32):** «那麼» you then/just «28» «號» arrive «法拉盛» «找» we
**Alternatives:**
  1. (20%) «那麼» you then/just «28» «號» arrive «法拉盛» «找» we
  2. (20%) «那麼» you exactly «28» «號» arrive «法拉盛» «找» we
  3. (20%) «那麼» you as_soon_as «28» «號» arrive «法拉盛» «找» we
  4. (20%) «那麼» you only «28» «號» arrive «法拉盛» «找» we
  5. (20%) «那麼» you then/just «28» «號» succeed «法拉盛» «找» we
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)

### [3/24 11:34 AM]
**Chinese:** 這些工作給專業的人做比較好、
**Primary (H=2.00):** «這些» work «給» «專業» «人» do/make «比較» good «、»
**Alternatives:**
  1. (25%) «這些» work «給» «專業» «人» do/make «比較» good «、»
  2. (25%) «這些» work «給» «專業» «人» work_as «比較» good «、»
  3. (25%) «這些» work «給» «專業» «人» conduct «比較» good «、»
  4. (25%) «這些» work «給» «專業» «人» do/make «比較» ok/agreed «、»
**Ambiguities detected:**
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/24 11:34 AM]
**Chinese:** 穿的隨性就好、
**Primary (H=2.32):** [I, 36%] «穿» «隨性» then/just good «、»
**Alternatives:**
  1. (15%) [I, 36%] «穿» «隨性» then/just good «、»
  2. (15%) [I, 36%] «穿» «隨性» exactly good «、»
  3. (15%) [I, 36%] «穿» «隨性» as_soon_as good «、»
  4. (15%) [I, 36%] «穿» «隨性» only good «、»
  5. (15%) [I, 36%] «穿» «隨性» then/just ok/agreed «、»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/24 1:05 PM]
**Chinese:** 那一對夫妻、我也是沒看過頭一次要跟他們碰面、因為他們讓我搬去他們家、
**Primary (H=2.32):** «那» «一對» «夫妻» «、» I «也» is/am/are no/not look/see «頭» «一次» «要» «跟» they «碰面» «、» «因為» they «讓» I «搬去» they «家» «、»
**Alternatives:**
  1. (20%) «那» «一對» «夫妻» «、» I «也» is/am/are no/not look/see «頭» «一次» «要» «跟» they «碰面» «、» «因為» they «讓» I «搬去» they «家» «、»
  2. (20%) «那» «一對» «夫妻» «、» I «也» is/am/are no/not read «頭» «一次» «要» «跟» they «碰面» «、» «因為» they «讓» I «搬去» they «家» «、»
  3. (20%) «那» «一對» «夫妻» «、» I «也» is/am/are no/not visit «頭» «一次» «要» «跟» they «碰面» «、» «因為» they «讓» I «搬去» they «家» «、»
  4. (20%) «那» «一對» «夫妻» «、» I «也» is/am/are no/not think/consider «頭» «一次» «要» «跟» they «碰面» «、» «因為» they «讓» I «搬去» they «家» «、»
  5. (20%) «那» «一對» «夫妻» «、» I «也» is/am/are no/not watch «頭» «一次» «要» «跟» they «碰面» «、» «因為» they «讓» I «搬去» they «家» «、»
**Ambiguities detected:**
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [3/24 1:24 PM]
**Chinese:** 沒事，大家就是像好朋友一樣一起碰面吃吃飯、聊聊天
**Primary (H=2.12):** [I, 36%] it's nothing/no problem «，» everyone «就是» «像» good friend «一樣» «一起» «碰面» eat eat rice/meal «、» «聊聊天»
**Alternatives:**
  1. (27%) [I, 36%] it's nothing/no problem «，» everyone «就是» «像» good friend «一樣» «一起» «碰面» eat eat rice/meal «、» «聊聊天»
  2. (27%) [I, 36%] it's nothing/no problem «，» everyone «就是» «像» ok/agreed friend «一樣» «一起» «碰面» eat eat rice/meal «、» «聊聊天»
  3. (26%) [you, 36%] it's nothing/no problem «，» everyone «就是» «像» good friend «一樣» «一起» «碰面» eat eat rice/meal «、» «聊聊天»
  4. (16%) [we, 22%] it's nothing/no problem «，» everyone «就是» «像» good friend «一樣» «一起» «碰面» eat eat rice/meal «、» «聊聊天»
  5. (3%) [they, 5%] it's nothing/no problem «，» everyone «就是» «像» good friend «一樣» «一起» «碰面» eat eat rice/meal «、» «聊聊天»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/24 1:24 PM]
**Chinese:** 最主要給你看看那裡的市場可以做的話、我就會開始規劃、起先會先給你世代產品再說、
**Primary (H=2.32):** «最» «主要» «給» you «看看» «那裡» «市場» «可以» do/make «話» «、» I then/just «會» «開始» «規劃» «、» «起先» «會» «先» «給» you «世代» product «再» say/speak «、»
**Alternatives:**
  1. (12%) «最» «主要» «給» you «看看» «那裡» «市場» «可以» do/make «話» «、» I then/just «會» «開始» «規劃» «、» «起先» «會» «先» «給» you «世代» product «再» say/speak «、»
  2. (12%) «最» «主要» «給» you «看看» «那裡» «市場» «可以» work_as «話» «、» I then/just «會» «開始» «規劃» «、» «起先» «會» «先» «給» you «世代» product «再» say/speak «、»
  3. (12%) «最» «主要» «給» you «看看» «那裡» «市場» «可以» conduct «話» «、» I then/just «會» «開始» «規劃» «、» «起先» «會» «先» «給» you «世代» product «再» say/speak «、»
  4. (12%) «最» «主要» «給» you «看看» «那裡» «市場» «可以» do/make «話» «、» I exactly «會» «開始» «規劃» «、» «起先» «會» «先» «給» you «世代» product «再» say/speak «、»
  5. (12%) «最» «主要» «給» you «看看» «那裡» «市場» «可以» do/make «話» «、» I as_soon_as «會» «開始» «規劃» «、» «起先» «會» «先» «給» you «世代» product «再» say/speak «、»
**Ambiguities detected:**
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to

### [3/24 1:24 PM]
**Chinese:** 尤其是你們有身體症狀的人、戴起來感覺會更快發現哪裡改善了、身體沒狀況的人？帶了也是養生
**Primary (H=2.30):** [I, 36%] «尤其» is/am/are you all have body/health «症狀» «人» «、» wear «起來» «感覺» «會» «更快» «發現» «哪裡» improve [completed] «、» body/health «沒狀況» «人» «？» bring [completed] «也» is/am/are «養生»
**Alternatives:**
  1. (21%) [I, 36%] «尤其» is/am/are you all have body/health «症狀» «人» «、» wear «起來» «感覺» «會» «更快» «發現» «哪裡» improve [completed] «、» body/health «沒狀況» «人» «？» bring [completed] «也» is/am/are «養生»
  2. (21%) [I, 36%] «尤其» is/am/are you all have body/health «症狀» «人» «、» wear «起來» «感覺» «會» «更快» «發現» «哪裡» improve [completed] «、» body/health «沒狀況» «人» «？» wear [completed] «也» is/am/are «養生»
  3. (21%) [I, 36%] «尤其» is/am/are you all have body/health «症狀» «人» «、» wear «起來» «感覺» «會» «更快» «發現» «哪裡» improve [completed] «、» body/health «沒狀況» «人» «？» lead/guide [completed] «也» is/am/are «養生»
  4. (21%) [you, 36%] «尤其» is/am/are you all have body/health «症狀» «人» «、» wear «起來» «感覺» «會» «更快» «發現» «哪裡» improve [completed] «、» body/health «沒狀況» «人» «？» bring [completed] «也» is/am/are «養生»
  5. (13%) [we, 22%] «尤其» is/am/are you all have body/health «症狀» «人» «、» wear «起來» «感覺» «會» «更快» «發現» «哪裡» improve [completed] «、» body/health «沒狀況» «人» «？» bring [completed] «也» is/am/are «養生»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone

### [3/24 2:02 PM]
**Chinese:** 你先看你的身體狀況、哪裡有問題？就針對戴哪裡？
**Primary (H=2.32):** you «先» think/consider you body/health «狀況» «、» «哪裡» have «問題» «？» then/just «針對» wear «哪裡» «？»
**Alternatives:**
  1. (13%) you «先» think/consider you body/health «狀況» «、» «哪裡» have «問題» «？» then/just «針對» wear «哪裡» «？»
  2. (13%) you «先» think/consider you body/health «狀況» «、» «哪裡» have «問題» «？» exactly «針對» wear «哪裡» «？»
  3. (13%) you «先» think/consider you body/health «狀況» «、» «哪裡» have «問題» «？» as_soon_as «針對» wear «哪裡» «？»
  4. (13%) you «先» think/consider you body/health «狀況» «、» «哪裡» have «問題» «？» only «針對» wear «哪裡» «？»
  5. (12%) you «先» look/see you body/health «狀況» «、» «哪裡» have «問題» «？» then/just «針對» wear «哪裡» «？»
**Ambiguities detected:**
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/24 2:02 PM]
**Chinese:** 你就像是我的家人一樣、所以我才跟聊這麼多、帶著你們大家一起變健康、又可以自己賺錢、還幫助很多人一起賺錢
**Primary (H=2.32):** you then/just «像是» I family «一樣» «、» «所以» I «才» «跟聊» «這麼» «多» «、» «帶著» you all everyone «一起» «變» healthy «、» «又» «可以» oneself «賺» money «、» still «幫助» «很多» «人» «一起» «賺» money
**Alternatives:**
  1. (14%) you then/just «像是» I family «一樣» «、» «所以» I «才» «跟聊» «這麼» «多» «、» «帶著» you all everyone «一起» «變» healthy «、» «又» «可以» oneself «賺» money «、» still «幫助» «很多» «人» «一起» «賺» money
  2. (14%) you exactly «像是» I family «一樣» «、» «所以» I «才» «跟聊» «這麼» «多» «、» «帶著» you all everyone «一起» «變» healthy «、» «又» «可以» oneself «賺» money «、» still «幫助» «很多» «人» «一起» «賺» money
  3. (14%) you as_soon_as «像是» I family «一樣» «、» «所以» I «才» «跟聊» «這麼» «多» «、» «帶著» you all everyone «一起» «變» healthy «、» «又» «可以» oneself «賺» money «、» still «幫助» «很多» «人» «一起» «賺» money
  4. (14%) you only «像是» I family «一樣» «、» «所以» I «才» «跟聊» «這麼» «多» «、» «帶著» you all everyone «一起» «變» healthy «、» «又» «可以» oneself «賺» money «、» still «幫助» «很多» «人» «一起» «賺» money
  5. (14%) you then/just «像是» I family «一樣» «、» «所以» I «才» «跟聊» «這麼» «多» «、» «帶著» you all everyone «一起» «變» healthy «、» «又» «可以» oneself «賺» money «、» also «幫助» «很多» «人» «一起» «賺» money
**Ambiguities detected:**
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/24 2:02 PM]
**Chinese:** 很多人都有頸椎的問題、因為手機太文明了、太多人花時間再用手機、所以頸椎的問題更大、頸椎沒顧好的話、兩個手也會變麻掉、心臟就更不用說了、心臟是身體最重要的一部分、
**Primary (H=2.32):** «很多» «人» «都» have «頸椎» «問題» «、» «因為» «手機» «太» «文明» [completed] «、» «太» «多» «人花» time «再» «用» «手機» «、» «所以» «頸椎» «問題» «更» «大» «、» «頸椎» «沒顧» good «話» «、» «兩個» «手» «也» «會» «變» «麻掉» «、» «心臟» then/just «更» «不用» say/speak [completed] «、» «心臟» is/am/are body/health «最» important «一部分» «、»
**Alternatives:**
  1. (14%) «很多» «人» «都» have «頸椎» «問題» «、» «因為» «手機» «太» «文明» [completed] «、» «太» «多» «人花» time «再» «用» «手機» «、» «所以» «頸椎» «問題» «更» «大» «、» «頸椎» «沒顧» good «話» «、» «兩個» «手» «也» «會» «變» «麻掉» «、» «心臟» then/just «更» «不用» say/speak [completed] «、» «心臟» is/am/are body/health «最» important «一部分» «、»
  2. (14%) «很多» «人» «都» have «頸椎» «問題» «、» «因為» «手機» «太» «文明» [completed] «、» «太» «多» «人花» time «再» «用» «手機» «、» «所以» «頸椎» «問題» «更» «大» «、» «頸椎» «沒顧» ok/agreed «話» «、» «兩個» «手» «也» «會» «變» «麻掉» «、» «心臟» then/just «更» «不用» say/speak [completed] «、» «心臟» is/am/are body/health «最» important «一部分» «、»
  3. (14%) «很多» «人» «都» have «頸椎» «問題» «、» «因為» «手機» «太» «文明» [completed] «、» «太» «多» «人花» time «再» «用» «手機» «、» «所以» «頸椎» «問題» «更» «大» «、» «頸椎» «沒顧» good «話» «、» «兩個» «手» «也» «會» «變» «麻掉» «、» «心臟» exactly «更» «不用» say/speak [completed] «、» «心臟» is/am/are body/health «最» important «一部分» «、»
  4. (14%) «很多» «人» «都» have «頸椎» «問題» «、» «因為» «手機» «太» «文明» [completed] «、» «太» «多» «人花» time «再» «用» «手機» «、» «所以» «頸椎» «問題» «更» «大» «、» «頸椎» «沒顧» good «話» «、» «兩個» «手» «也» «會» «變» «麻掉» «、» «心臟» as_soon_as «更» «不用» say/speak [completed] «、» «心臟» is/am/are body/health «最» important «一部分» «、»
  5. (14%) «很多» «人» «都» have «頸椎» «問題» «、» «因為» «手機» «太» «文明» [completed] «、» «太» «多» «人花» time «再» «用» «手機» «、» «所以» «頸椎» «問題» «更» «大» «、» «頸椎» «沒顧» good «話» «、» «兩個» «手» «也» «會» «變» «麻掉» «、» «心臟» only «更» «不用» say/speak [completed] «、» «心臟» is/am/are body/health «最» important «一部分» «、»
**Ambiguities detected:**
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to

### [3/24 2:02 PM]
**Chinese:** 有好轉是好事、戴上量子環也可以保護身體、讓身體更健康、
**Primary (H=2.12):** [I, 36%] have good «轉» is/am/are «好事» «、» wear «上» «量子» «環» «也» «可以» «保護» body/health «、» «讓» body/health «更» healthy «、»
**Alternatives:**
  1. (27%) [I, 36%] have good «轉» is/am/are «好事» «、» wear «上» «量子» «環» «也» «可以» «保護» body/health «、» «讓» body/health «更» healthy «、»
  2. (27%) [I, 36%] have ok/agreed «轉» is/am/are «好事» «、» wear «上» «量子» «環» «也» «可以» «保護» body/health «、» «讓» body/health «更» healthy «、»
  3. (26%) [you, 36%] have good «轉» is/am/are «好事» «、» wear «上» «量子» «環» «也» «可以» «保護» body/health «、» «讓» body/health «更» healthy «、»
  4. (16%) [we, 22%] have good «轉» is/am/are «好事» «、» wear «上» «量子» «環» «也» «可以» «保護» body/health «、» «讓» body/health «更» healthy «、»
  5. (3%) [they, 5%] have good «轉» is/am/are «好事» «、» wear «上» «量子» «環» «也» «可以» «保護» body/health «、» «讓» body/health «更» healthy «、»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/24 2:02 PM]
**Chinese:** 頸椎這個地方是很重要、所以不要亂看醫生看對沒關係看錯就一輩子後悔了
**Primary (H=2.32):** «頸椎» «這個» «地方» is/am/are «很» important «、» «所以» «不要» «亂» look/see «醫生» «看對» no/not «關» «係» look/see «錯» then/just «一» «輩» «子» «後» «悔» [completed]
**Alternatives:**
  1. (7%) «頸椎» «這個» «地方» is/am/are «很» important «、» «所以» «不要» «亂» look/see «醫生» «看對» no/not «關» «係» look/see «錯» then/just «一» «輩» «子» «後» «悔» [completed]
  2. (7%) «頸椎» «這個» «地方» is/am/are «很» important «、» «所以» «不要» «亂» look/see «醫生» «看對» no/not «關» «係» look/see «錯» then/just «一» «輩» «子» «後» «悔» [completed]
  3. (7%) «頸椎» «這個» «地方» is/am/are «很» important «、» «所以» «不要» «亂» look/see «醫生» «看對» no/not «關» «係» look/see «錯» then/just «一» «輩» «子» «後» «悔» [completed]
  4. (7%) «頸椎» «這個» «地方» is/am/are «很» important «、» «所以» «不要» «亂» look/see «醫生» «看對» no/not «關» «係» look/see «錯» then/just «一» «輩» «子» «後» «悔» [completed]
  5. (7%) «頸椎» «這個» «地方» is/am/are «很» important «、» «所以» «不要» «亂» look/see «醫生» «看對» no/not «關» «係» look/see «錯» then/just «一» «輩» «子» «後» «悔» [completed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/24 2:02 PM]
**Chinese:** 這個老奶奶從年輕到老頭是頸椎的問題，你看他帶了不到半年頸椎變好了，人也不駝背了
**Primary (H=2.32):** «這個» «老奶奶» «從» «年» «輕» arrive «老頭» is/am/are «頸椎» «問題» «，» you look/see he bring [completed] «不到» «半年» «頸椎» «變好» [completed] «，» «人» «也» not «駝» «背» [completed]
**Alternatives:**
  1. (10%) «這個» «老奶奶» «從» «年» «輕» arrive «老頭» is/am/are «頸椎» «問題» «，» you look/see he bring [completed] «不到» «半年» «頸椎» «變好» [completed] «，» «人» «也» not «駝» «背» [completed]
  2. (10%) «這個» «老奶奶» «從» «年» «輕» succeed «老頭» is/am/are «頸椎» «問題» «，» you look/see he bring [completed] «不到» «半年» «頸椎» «變好» [completed] «，» «人» «也» not «駝» «背» [completed]
  3. (10%) «這個» «老奶奶» «從» «年» «輕» arrive «老頭» is/am/are «頸椎» «問題» «，» you read he bring [completed] «不到» «半年» «頸椎» «變好» [completed] «，» «人» «也» not «駝» «背» [completed]
  4. (10%) «這個» «老奶奶» «從» «年» «輕» arrive «老頭» is/am/are «頸椎» «問題» «，» you visit he bring [completed] «不到» «半年» «頸椎» «變好» [completed] «，» «人» «也» not «駝» «背» [completed]
  5. (10%) «這個» «老奶奶» «從» «年» «輕» arrive «老頭» is/am/are «頸椎» «問題» «，» you think/consider he bring [completed] «不到» «半年» «頸椎» «變好» [completed] «，» «人» «也» not «駝» «背» [completed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone

### [3/24 2:22 PM]
**Chinese:** 這樣很好啊
**Primary (H=2.32):** «這樣» «很» good !
**Alternatives:**
  1. (20%) «這樣» «很» good !
  2. (20%) «這樣» «很» ok/agreed !
  3. (20%) «這樣» «很» good
  4. (20%) «這樣» «很» good (oh!)
  5. (20%) «這樣» «很» good (come on)
**Ambiguities detected:**
  - particle on **啊**: exclamation: Wow / emphasis, filler: Softening / conversational filler, realization: Oh! / I see, urging: Come on / hurry up
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/24 4:44 PM]
**Chinese:** 我們還在忙
**Primary (H=2.00):** we still «在» busy
**Alternatives:**
  1. (25%) we still «在» busy
  2. (25%) we also «在» busy
  3. (25%) we even «在» busy
  4. (25%) we fairly «在» busy
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/24 7:54 PM]
**Chinese:** 離這裡要三四個小時，對吧？
**Primary (H=2.26):** [you, 56%] «離» «這裡» «要» «三四» «個» «小» «時» «，» right/correct (let's / how about) «？»
**Alternatives:**
  1. (21%) [you, 56%] «離» «這裡» «要» «三四» «個» «小» «時» «，» right/correct (let's / how about) «？»
  2. (21%) [you, 56%] «離» «這裡» «要» «三四» «個» «小» «時» «，» right/correct (fine / I suppose) «？»
  3. (21%) [you, 56%] «離» «這裡» «要» «三四» «個» «小» «時» «，» right/correct (I think / probably) «？»
  4. (21%) [you, 56%] «離» «這裡» «要» «三四» «個» «小» «時» «，» right/correct (you should) «？»
  5. (8%) [I, 22%] «離» «這裡» «要» «三四» «個» «小» «時» «，» right/correct (let's / how about) «？»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **吧**: suggestion: Let's... / How about..., concession: Fine, go ahead / I suppose so, uncertainty: I think so / probably, softened_command: You should... (softened)

### [3/24 7:54 PM]
**Chinese:** 還沒
**Primary (H=2.32):** [I, 36%] still no/not
**Alternatives:**
  1. (17%) [I, 36%] still no/not
  2. (17%) [I, 36%] also no/not
  3. (17%) [I, 36%] even no/not
  4. (17%) [I, 36%] fairly no/not
  5. (17%) [you, 36%] still no/not
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/24 7:54 PM]
**Chinese:** 你現在還在賓州嗎？
**Primary (H=2.32):** you now still «在» «賓州» «？»
**Alternatives:**
  1. (20%) you now still «在» «賓州» «？»
  2. (20%) you now also «在» «賓州» «？»
  3. (20%) you now even «在» «賓州» «？»
  4. (20%) you now fairly «在» «賓州» «？»
  5. (20%) you now still «在» «賓州» «？»
**Ambiguities detected:**
  - particle on **嗎**: yes_no_question: Is it? / Did you?, rhetorical: Isn't it obvious?
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/24 7:54 PM]
**Chinese:** 現在都八點了，那你就住在賓州，不然回來你家不是凌晨了嗎？
**Primary (H=2.32):** now «都» «八點» [completed] «，» «那» you then/just live «在» «賓州» «，» «不然» come back «你家» «不是» «凌晨» [completed] «？»
**Alternatives:**
  1. (20%) now «都» «八點» [completed] «，» «那» you then/just live «在» «賓州» «，» «不然» come back «你家» «不是» «凌晨» [completed] «？»
  2. (20%) now «都» «八點» [completed] «，» «那» you exactly live «在» «賓州» «，» «不然» come back «你家» «不是» «凌晨» [completed] «？»
  3. (20%) now «都» «八點» [completed] «，» «那» you as_soon_as live «在» «賓州» «，» «不然» come back «你家» «不是» «凌晨» [completed] «？»
  4. (20%) now «都» «八點» [completed] «，» «那» you only live «在» «賓州» «，» «不然» come back «你家» «不是» «凌晨» [completed] «？»
  5. (20%) now «都» «八點» [completed] «，» «那» you then/just live «在» «賓州» «，» «不然» come back «你家» «不是» «凌晨» [completed] «？»
**Ambiguities detected:**
  - particle on **嗎**: yes_no_question: Is it? / Did you?, rhetorical: Isn't it obvious?
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/24 8:45 PM]
**Chinese:** 我們還在上班啊，快下班了
**Primary (H=2.32):** we still «在» «上班» ! «，» «快下班» [completed]
**Alternatives:**
  1. (17%) we still «在» «上班» ! «，» «快下班» [completed]
  2. (17%) we also «在» «上班» ! «，» «快下班» [completed]
  3. (17%) we even «在» «上班» ! «，» «快下班» [completed]
  4. (17%) we fairly «在» «上班» ! «，» «快下班» [completed]
  5. (16%) we still «在» «上班» ! «，» «快下班» [now/changed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/24 9:36 PM]
**Chinese:** 我們還沒回去纽约啊
**Primary (H=2.32):** we still no/not go back «纽约» !
**Alternatives:**
  1. (14%) we still no/not go back «纽约» !
  2. (14%) we also no/not go back «纽约» !
  3. (14%) we even no/not go back «纽约» !
  4. (14%) we fairly no/not go back «纽约» !
  5. (14%) we still no/not go back «纽约»
**Ambiguities detected:**
  - particle on **啊**: exclamation: Wow / emphasis, filler: Softening / conversational filler, realization: Oh! / I see, urging: Come on / hurry up
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/24 9:36 PM]
**Chinese:** 今天還沒跟家人聊天、
**Primary (H=2.00):** today still no/not «跟» family «聊天» «、»
**Alternatives:**
  1. (25%) today still no/not «跟» family «聊天» «、»
  2. (25%) today also no/not «跟» family «聊天» «、»
  3. (25%) today even no/not «跟» family «聊天» «、»
  4. (25%) today fairly no/not «跟» family «聊天» «、»
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/24 9:36 PM]
**Chinese:** 這個就是我去吃飯攝影給我家人看的、本來我要加盟，還好沒加盟
**Primary (H=2.32):** «這個» «就是» I go eat rice/meal «攝» «影給» «我家» «人» look/see «、» «本來» I «要» «加盟» «，» still good no/not «加盟»
**Alternatives:**
  1. (11%) «這個» «就是» I go eat rice/meal «攝» «影給» «我家» «人» look/see «、» «本來» I «要» «加盟» «，» still good no/not «加盟»
  2. (11%) «這個» «就是» I go eat rice/meal «攝» «影給» «我家» «人» read «、» «本來» I «要» «加盟» «，» still good no/not «加盟»
  3. (11%) «這個» «就是» I go eat rice/meal «攝» «影給» «我家» «人» visit «、» «本來» I «要» «加盟» «，» still good no/not «加盟»
  4. (11%) «這個» «就是» I go eat rice/meal «攝» «影給» «我家» «人» think/consider «、» «本來» I «要» «加盟» «，» still good no/not «加盟»
  5. (11%) «這個» «就是» I go eat rice/meal «攝» «影給» «我家» «人» watch «、» «本來» I «要» «加盟» «，» still good no/not «加盟»
**Ambiguities detected:**
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/24 9:36 PM]
**Chinese:** 好喝的日本抹茶、還有抹茶粉做的拉麵
**Primary (H=2.32):** [I, 36%] «好喝» «日本» «抹» «茶» «、» still have «抹» «茶» «粉» do/make «拉» «麵»
**Alternatives:**
  1. (13%) [I, 36%] «好喝» «日本» «抹» «茶» «、» still have «抹» «茶» «粉» do/make «拉» «麵»
  2. (13%) [I, 36%] «好喝» «日本» «抹» «茶» «、» also have «抹» «茶» «粉» do/make «拉» «麵»
  3. (13%) [I, 36%] «好喝» «日本» «抹» «茶» «、» even have «抹» «茶» «粉» do/make «拉» «麵»
  4. (13%) [I, 36%] «好喝» «日本» «抹» «茶» «、» fairly have «抹» «茶» «粉» do/make «拉» «麵»
  5. (13%) [I, 36%] «好喝» «日本» «抹» «茶» «、» still have «抹» «茶» «粉» work_as «拉» «麵»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)

### [3/24 9:36 PM]
**Chinese:** 最好的就是做我們的產品、自己帶著健康幫助別人健康、又幫助別人賺錢
**Primary (H=2.17):** [you, 56%] «最好» «就是» do/make we product «、» oneself «帶著» healthy «幫助» «別人» healthy «、» «又» «幫助» «別人» «賺» money
**Alternatives:**
  1. (26%) [you, 56%] «最好» «就是» do/make we product «、» oneself «帶著» healthy «幫助» «別人» healthy «、» «又» «幫助» «別人» «賺» money
  2. (26%) [you, 56%] «最好» «就是» work_as we product «、» oneself «帶著» healthy «幫助» «別人» healthy «、» «又» «幫助» «別人» «賺» money
  3. (26%) [you, 56%] «最好» «就是» conduct we product «、» oneself «帶著» healthy «幫助» «別人» healthy «、» «又» «幫助» «別人» «賺» money
  4. (10%) [I, 22%] «最好» «就是» do/make we product «、» oneself «帶著» healthy «幫助» «別人» healthy «、» «又» «幫助» «別人» «賺» money
  5. (8%) [we, 17%] «最好» «就是» do/make we product «、» oneself «帶著» healthy «幫助» «別人» healthy «、» «又» «幫助» «別人» «賺» money
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)

### [3/24 9:36 PM]
**Chinese:** 因為那一家很健康、是一家很好的餐廳、我本來也要加盟還好沒加盟，她在紐約已經開了七年了
**Primary (H=2.32):** «因為» «那» «一家» «很» healthy «、» is/am/are «一家» «很好» «餐廳» «、» I «本來» «也» «要» «加盟» still good no/not «加盟» «，» she «在» New York «已經» open [completed] «七年» [completed]
**Alternatives:**
  1. (9%) «因為» «那» «一家» «很» healthy «、» is/am/are «一家» «很好» «餐廳» «、» I «本來» «也» «要» «加盟» still good no/not «加盟» «，» she «在» New York «已經» open [completed] «七年» [completed]
  2. (9%) «因為» «那» «一家» «很» healthy «、» is/am/are «一家» «很好» «餐廳» «、» I «本來» «也» «要» «加盟» also good no/not «加盟» «，» she «在» New York «已經» open [completed] «七年» [completed]
  3. (9%) «因為» «那» «一家» «很» healthy «、» is/am/are «一家» «很好» «餐廳» «、» I «本來» «也» «要» «加盟» even good no/not «加盟» «，» she «在» New York «已經» open [completed] «七年» [completed]
  4. (9%) «因為» «那» «一家» «很» healthy «、» is/am/are «一家» «很好» «餐廳» «、» I «本來» «也» «要» «加盟» fairly good no/not «加盟» «，» she «在» New York «已經» open [completed] «七年» [completed]
  5. (9%) «因為» «那» «一家» «很» healthy «、» is/am/are «一家» «很好» «餐廳» «、» I «本來» «也» «要» «加盟» still ok/agreed no/not «加盟» «，» she «在» New York «已經» open [completed] «七年» [completed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **開**: open: To open, start/operate: To start a business/operate, drive: To drive a vehicle, turn_on: To turn on/switch on

### [3/24 9:36 PM]
**Chinese:** 現在全世界的時機不好、所以不要做一些太辛苦的事情、你自己體驗帶看看、到時候再纽约跟我們一起工作吧、可以賺薪水又可以賺紅利、公司，每個月會補獎金
**Primary (H=2.32):** now «全世界» «時機» «不好» «、» «所以» «不要» do/make «一些» «太» hard/difficult «事情» «、» you oneself «體驗» bring «看看» «、» arrive «時候» «再» «纽约» «跟» we «一起» work (let's / how about) «、» «可以» «賺» salary «又» «可以» «賺» «紅利» «、» company «，» «每個» «月會» «補獎» «金»
**Alternatives:**
  1. (17%) now «全世界» «時機» «不好» «、» «所以» «不要» do/make «一些» «太» hard/difficult «事情» «、» you oneself «體驗» bring «看看» «、» arrive «時候» «再» «纽约» «跟» we «一起» work (let's / how about) «、» «可以» «賺» salary «又» «可以» «賺» «紅利» «、» company «，» «每個» «月會» «補獎» «金»
  2. (17%) now «全世界» «時機» «不好» «、» «所以» «不要» work_as «一些» «太» hard/difficult «事情» «、» you oneself «體驗» bring «看看» «、» arrive «時候» «再» «纽约» «跟» we «一起» work (let's / how about) «、» «可以» «賺» salary «又» «可以» «賺» «紅利» «、» company «，» «每個» «月會» «補獎» «金»
  3. (17%) now «全世界» «時機» «不好» «、» «所以» «不要» conduct «一些» «太» hard/difficult «事情» «、» you oneself «體驗» bring «看看» «、» arrive «時候» «再» «纽约» «跟» we «一起» work (let's / how about) «、» «可以» «賺» salary «又» «可以» «賺» «紅利» «、» company «，» «每個» «月會» «補獎» «金»
  4. (17%) now «全世界» «時機» «不好» «、» «所以» «不要» do/make «一些» «太» hard/difficult «事情» «、» you oneself «體驗» wear «看看» «、» arrive «時候» «再» «纽约» «跟» we «一起» work (let's / how about) «、» «可以» «賺» salary «又» «可以» «賺» «紅利» «、» company «，» «每個» «月會» «補獎» «金»
  5. (17%) now «全世界» «時機» «不好» «、» «所以» «不要» do/make «一些» «太» hard/difficult «事情» «、» you oneself «體驗» lead/guide «看看» «、» arrive «時候» «再» «纽约» «跟» we «一起» work (let's / how about) «、» «可以» «賺» salary «又» «可以» «賺» «紅利» «、» company «，» «每個» «月會» «補獎» «金»
**Ambiguities detected:**
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)

### [3/24 9:36 PM]
**Chinese:** 不要浪費錢去想要做一些、太傷腦筋的工作、做量子環最簡單又不傷腦筋，又可以幫助別人健康跟賺錢的工作
**Primary (H=2.32):** «不要» «浪費» money go «想要» do/make «一些» «、» «太傷» «腦筋» work «、» do/make «量子» «環» «最» simple «又» «不傷» «腦筋» «，» «又» «可以» «幫助» «別人» healthy «跟» «賺» money work
**Alternatives:**
  1. (20%) «不要» «浪費» money go «想要» do/make «一些» «、» «太傷» «腦筋» work «、» do/make «量子» «環» «最» simple «又» «不傷» «腦筋» «，» «又» «可以» «幫助» «別人» healthy «跟» «賺» money work
  2. (20%) «不要» «浪費» money go «想要» do/make «一些» «、» «太傷» «腦筋» work «、» do/make «量子» «環» «最» simple «又» «不傷» «腦筋» «，» «又» «可以» «幫助» «別人» healthy «跟» «賺» money work
  3. (20%) «不要» «浪費» money go «想要» do/make «一些» «、» «太傷» «腦筋» work «、» do/make «量子» «環» «最» simple «又» «不傷» «腦筋» «，» «又» «可以» «幫助» «別人» healthy «跟» «賺» money work
  4. (20%) «不要» «浪費» money go «想要» work_as «一些» «、» «太傷» «腦筋» work «、» work_as «量子» «環» «最» simple «又» «不傷» «腦筋» «，» «又» «可以» «幫助» «別人» healthy «跟» «賺» money work
  5. (20%) «不要» «浪費» money go «想要» conduct «一些» «、» «太傷» «腦筋» work «、» conduct «量子» «環» «最» simple «又» «不傷» «腦筋» «，» «又» «可以» «幫助» «別人» healthy «跟» «賺» money work
**Ambiguities detected:**
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)
  - polysemy on **做**: do/make: To do/make, work_as: To work as/be (profession), conduct: To conduct (business)

### [3/24 10:14 PM]
**Chinese:** 你不用問你的朋友、只要你帶的身體有改善，你自己就知道、我們又不是要賣你的朋友、是在紐約那邊的人、那裡的所有華人都很注重健康的、他們也是喜歡健康喜歡賺錢的、你也不用去推銷他們自己帶就會自己來買了
**Primary (H=2.32):** you «不用» «問» you friend «、» «只要» you bring body/health have improve «，» you oneself then/just know «、» we «又» «不是» «要» sell you friend «、» is/am/are «在» New York «那邊» «人» «、» «那裡» «所有» «華» «人» «都» «很» «注重» healthy «、» they «也» is/am/are like healthy like «賺» money «、» you «也» «不用» go «推銷» they oneself bring then/just «會» oneself come buy [completed]
**Alternatives:**
  1. (8%) you «不用» «問» you friend «、» «只要» you bring body/health have improve «，» you oneself then/just know «、» we «又» «不是» «要» sell you friend «、» is/am/are «在» New York «那邊» «人» «、» «那裡» «所有» «華» «人» «都» «很» «注重» healthy «、» they «也» is/am/are like healthy like «賺» money «、» you «也» «不用» go «推銷» they oneself bring then/just «會» oneself come buy [completed]
  2. (8%) you «不用» «問» you friend «、» «只要» you bring body/health have improve «，» you oneself then/just know «、» we «又» «不是» «要» sell you friend «、» is/am/are «在» New York «那邊» «人» «、» «那裡» «所有» «華» «人» «都» «很» «注重» healthy «、» they «也» is/am/are like healthy like «賺» money «、» you «也» «不用» go «推銷» they oneself bring then/just «會» oneself come buy [completed]
  3. (8%) you «不用» «問» you friend «、» «只要» you bring body/health have improve «，» you oneself then/just know «、» we «又» «不是» «要» sell you friend «、» is/am/are «在» New York «那邊» «人» «、» «那裡» «所有» «華» «人» «都» «很» «注重» healthy «、» they «也» is/am/are like healthy like «賺» money «、» you «也» «不用» go «推銷» they oneself bring then/just «會» oneself come buy [completed]
  4. (8%) you «不用» «問» you friend «、» «只要» you bring body/health have improve «，» you oneself then/just know «、» we «又» «不是» «要» sell you friend «、» is/am/are «在» New York «那邊» «人» «、» «那裡» «所有» «華» «人» «都» «很» «注重» healthy «、» they «也» is/am/are like healthy like «賺» money «、» you «也» «不用» go «推銷» they oneself bring then/just «會» oneself come buy [completed]
  5. (8%) you «不用» «問» you friend «、» «只要» you bring body/health have improve «，» you oneself then/just know «、» we «又» «不是» «要» sell you friend «、» is/am/are «在» New York «那邊» «人» «、» «那裡» «所有» «華» «人» «都» «很» «注重» healthy «、» they «也» is/am/are like healthy like «賺» money «、» you «也» «不用» go «推銷» they oneself bring then/just «會» oneself come buy [completed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **帶**: bring: To bring/carry, wear: To wear (accessories), lead/guide: To lead/guide someone
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/24 10:40 PM]
**Chinese:** 沒事，不用想那麼多順其自然的工作就好、
**Primary (H=2.32):** [I, 36%] it's nothing/no problem «，» «不用» want/think «那麼» «多» «順其» «自然» work then/just good «、»
**Alternatives:**
  1. (15%) [I, 36%] it's nothing/no problem «，» «不用» want/think «那麼» «多» «順其» «自然» work then/just good «、»
  2. (15%) [I, 36%] it's nothing/no problem «，» «不用» want/think «那麼» «多» «順其» «自然» work exactly good «、»
  3. (15%) [I, 36%] it's nothing/no problem «，» «不用» want/think «那麼» «多» «順其» «自然» work as_soon_as good «、»
  4. (15%) [I, 36%] it's nothing/no problem «，» «不用» want/think «那麼» «多» «順其» «自然» work only good «、»
  5. (15%) [I, 36%] it's nothing/no problem «，» «不用» want/think «那麼» «多» «順其» «自然» work then/just ok/agreed «、»
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/24 10:40 PM]
**Chinese:** 你到時候去看看看那裡的環境、喜歡的話以後可以跟我們一起工作、
**Primary (H=2.32):** you arrive «時候» go «看看» look/see «那裡» «環境» «、» like «話» «以» «後» «可以» «跟» we «一起» work «、»
**Alternatives:**
  1. (17%) you arrive «時候» go «看看» look/see «那裡» «環境» «、» like «話» «以» «後» «可以» «跟» we «一起» work «、»
  2. (17%) you succeed «時候» go «看看» look/see «那裡» «環境» «、» like «話» «以» «後» «可以» «跟» we «一起» work «、»
  3. (17%) you arrive «時候» go «看看» read «那裡» «環境» «、» like «話» «以» «後» «可以» «跟» we «一起» work «、»
  4. (17%) you arrive «時候» go «看看» visit «那裡» «環境» «、» like «話» «以» «後» «可以» «跟» we «一起» work «、»
  5. (17%) you arrive «時候» go «看看» think/consider «那裡» «環境» «、» like «話» «以» «後» «可以» «跟» we «一起» work «、»
**Ambiguities detected:**
  - polysemy on **到**: arrive: To arrive at, succeed: Successfully (complement)
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [3/24 11:15 PM]
**Chinese:** 醫生說總共電療45次就可以了
**Primary (H=2.32):** «醫生» say/speak «總共» «電療» «45» «次» then/just «可以» [completed]
**Alternatives:**
  1. (13%) «醫生» say/speak «總共» «電療» «45» «次» then/just «可以» [completed]
  2. (13%) «醫生» scold «總共» «電療» «45» «次» then/just «可以» [completed]
  3. (13%) «醫生» mean «總共» «電療» «45» «次» then/just «可以» [completed]
  4. (13%) «醫生» say/speak «總共» «電療» «45» «次» exactly «可以» [completed]
  5. (13%) «醫生» say/speak «總共» «電療» «45» «次» as_soon_as «可以» [completed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely

### [3/24 11:15 PM]
**Chinese:** 台灣的醫學很厲害，別擔心、電療45次以後就好了
**Primary (H=2.32):** Taiwan «醫學» «很» impressive «，» «別» «擔心» «、» «電療» «45» «次» «以» «後» then/just good [completed]
**Alternatives:**
  1. (15%) Taiwan «醫學» «很» impressive «，» «別» «擔心» «、» «電療» «45» «次» «以» «後» then/just good [completed]
  2. (15%) Taiwan «醫學» «很» impressive «，» «別» «擔心» «、» «電療» «45» «次» «以» «後» exactly good [completed]
  3. (15%) Taiwan «醫學» «很» impressive «，» «別» «擔心» «、» «電療» «45» «次» «以» «後» as_soon_as good [completed]
  4. (15%) Taiwan «醫學» «很» impressive «，» «別» «擔心» «、» «電療» «45» «次» «以» «後» only good [completed]
  5. (15%) Taiwan «醫學» «很» impressive «，» «別» «擔心» «、» «電療» «45» «次» «以» «後» then/just ok/agreed [completed]
**Ambiguities detected:**
  - particle on **了**: completed_action: Action completed / done, change_of_state: Now... / things have changed, excessive: Too much / overly
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

### [3/24 11:15 PM]
**Chinese:** 是去年台灣採收荔枝、她的媽媽幫她拍照、跟錄影給我們家人看
**Primary (H=2.32):** [I, 36%] is/am/are «去年» Taiwan «採收» «荔枝» «、» she mom help she «拍照» «、» «跟錄» «影給» we family look/see
**Alternatives:**
  1. (15%) [I, 36%] is/am/are «去年» Taiwan «採收» «荔枝» «、» she mom help she «拍照» «、» «跟錄» «影給» we family look/see
  2. (15%) [I, 36%] is/am/are «去年» Taiwan «採收» «荔枝» «、» she mom help she «拍照» «、» «跟錄» «影給» we family read
  3. (15%) [I, 36%] is/am/are «去年» Taiwan «採收» «荔枝» «、» she mom help she «拍照» «、» «跟錄» «影給» we family visit
  4. (15%) [I, 36%] is/am/are «去年» Taiwan «採收» «荔枝» «、» she mom help she «拍照» «、» «跟錄» «影給» we family think/consider
  5. (15%) [I, 36%] is/am/are «去年» Taiwan «採收» «荔枝» «、» she mom help she «拍照» «、» «跟錄» «影給» we family watch
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [3/24 11:15 PM]
**Chinese:** 那時候是去年的六月、爸爸還沒有檢查出身體的狀況、是後來醫院檢查出來才知道爸爸的狀況
**Primary (H=2.00):** «那» «時候» is/am/are «去年» «六月» «、» dad still don't have «檢查» «出身» «體» «狀況» «、» is/am/are «後» come «醫院» «檢» «查出» come «才» know dad «狀況»
**Alternatives:**
  1. (25%) «那» «時候» is/am/are «去年» «六月» «、» dad still don't have «檢查» «出身» «體» «狀況» «、» is/am/are «後» come «醫院» «檢» «查出» come «才» know dad «狀況»
  2. (25%) «那» «時候» is/am/are «去年» «六月» «、» dad also don't have «檢查» «出身» «體» «狀況» «、» is/am/are «後» come «醫院» «檢» «查出» come «才» know dad «狀況»
  3. (25%) «那» «時候» is/am/are «去年» «六月» «、» dad even don't have «檢查» «出身» «體» «狀況» «、» is/am/are «後» come «醫院» «檢» «查出» come «才» know dad «狀況»
  4. (25%) «那» «時候» is/am/are «去年» «六月» «、» dad fairly don't have «檢查» «出身» «體» «狀況» «、» is/am/are «後» come «醫院» «檢» «查出» come «才» know dad «狀況»
**Ambiguities detected:**
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/25 3:00 PM]
**Chinese:** 好的，我進去看看看
**Primary (H=2.32):** good «，» I «進去» «看看» look/see
**Alternatives:**
  1. (17%) good «，» I «進去» «看看» look/see
  2. (17%) ok/agreed «，» I «進去» «看看» look/see
  3. (17%) good «，» I «進去» «看看» read
  4. (17%) good «，» I «進去» «看看» visit
  5. (17%) good «，» I «進去» «看看» think/consider
**Ambiguities detected:**
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [3/25 3:00 PM]
**Chinese:** 還沒有吃、我們還在忙
**Primary (H=2.32):** [I, 36%] still don't have eat «、» we still «在» busy
**Alternatives:**
  1. (11%) [I, 36%] still don't have eat «、» we still «在» busy
  2. (11%) [I, 36%] still don't have eat «、» we still «在» busy
  3. (11%) [I, 36%] still don't have eat «、» we still «在» busy
  4. (11%) [I, 36%] still don't have eat «、» we still «在» busy
  5. (11%) [I, 36%] also don't have eat «、» we also «在» busy
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably

### [3/25 3:00 PM]
**Chinese:** 你回去有空再看、不著急
**Primary (H=2.32):** you go back «有空» «再» look/see «、» «不著» «急»
**Alternatives:**
  1. (20%) you go back «有空» «再» look/see «、» «不著» «急»
  2. (20%) you go back «有空» «再» read «、» «不著» «急»
  3. (20%) you go back «有空» «再» visit «、» «不著» «急»
  4. (20%) you go back «有空» «再» think/consider «、» «不著» «急»
  5. (20%) you go back «有空» «再» watch «、» «不著» «急»
**Ambiguities detected:**
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [3/25 6:06 PM]
**Chinese:** 不著急、有空再看
**Primary (H=2.32):** [I, 36%] «不著» «急» «、» «有空» «再» look/see
**Alternatives:**
  1. (15%) [I, 36%] «不著» «急» «、» «有空» «再» look/see
  2. (15%) [I, 36%] «不著» «急» «、» «有空» «再» read
  3. (15%) [I, 36%] «不著» «急» «、» «有空» «再» visit
  4. (15%) [I, 36%] «不著» «急» «、» «有空» «再» think/consider
  5. (15%) [I, 36%] «不著» «急» «、» «有空» «再» watch
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **看**: look/see: To look at/see, read: To read, visit: To visit (a doctor), think/consider: To think/consider (看看)

### [3/25 10:28 PM]
**Chinese:** 我們回來老闆娘家、跟我爸爸媽媽視訊，忘了跟你打電話
**Primary (H=2.32):** we come back «老» «闆» «娘家» «、» «跟» I dad mom «視訊» «，» «忘» [completed] «跟» you hit/strike «電話»
**Alternatives:**
  1. (20%) we come back «老» «闆» «娘家» «、» «跟» I dad mom «視訊» «，» «忘» [completed] «跟» you hit/strike «電話»
  2. (20%) we come back «老» «闆» «娘家» «、» «跟» I dad mom «視訊» «，» «忘» [completed] «跟» you make_phone_call «電話»
  3. (20%) we come back «老» «闆» «娘家» «、» «跟» I dad mom «視訊» «，» «忘» [completed] «跟» you play «電話»
  4. (20%) we come back «老» «闆» «娘家» «、» «跟» I dad mom «視訊» «，» «忘» [completed] «跟» you type/work «電話»
  5. (20%) we come back «老» «闆» «娘家» «、» «跟» I dad mom «視訊» «，» «忘» [completed] «跟» you get/buy «電話»
**Ambiguities detected:**
  - polysemy on **打**: hit/strike: Physical hitting, make_phone_call: To make a call, play: To play (games/sports), type/work: To do/work on

### [3/25 10:28 PM]
**Chinese:** 租一個房子、貴嗎
**Primary (H=2.12):** [I, 36%] rent «一個» «房子» «、» expensive
**Alternatives:**
  1. (27%) [I, 36%] rent «一個» «房子» «、» expensive
  2. (26%) [you, 36%] rent «一個» «房子» «、» expensive
  3. (26%) [I, 36%] rent «一個» «房子» «、» expensive
  4. (16%) [we, 22%] rent «一個» «房子» «、» expensive
  5. (3%) [they, 5%] rent «一個» «房子» «、» expensive
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **嗎**: yes_no_question: Is it? / Did you?, rhetorical: Isn't it obvious?

### [3/25 10:28 PM]
**Chinese:** 不著急、等你先試戴量子環反應如何在說、我在紐約要開始運作前一個月告知你
**Primary (H=2.17):** [you, 56%] «不著» «急» «、» you «先» «試戴» «量子» «環» «反應» «如何» «在» say/speak «、» I «在» New York «要» «開始» «運作» «前» «一個» «月» «告知» you
**Alternatives:**
  1. (26%) [you, 56%] «不著» «急» «、» you «先» «試戴» «量子» «環» «反應» «如何» «在» say/speak «、» I «在» New York «要» «開始» «運作» «前» «一個» «月» «告知» you
  2. (26%) [you, 56%] «不著» «急» «、» you «先» «試戴» «量子» «環» «反應» «如何» «在» scold «、» I «在» New York «要» «開始» «運作» «前» «一個» «月» «告知» you
  3. (26%) [you, 56%] «不著» «急» «、» you «先» «試戴» «量子» «環» «反應» «如何» «在» mean «、» I «在» New York «要» «開始» «運作» «前» «一個» «月» «告知» you
  4. (10%) [I, 22%] «不著» «急» «、» you «先» «試戴» «量子» «環» «反應» «如何» «在» say/speak «、» I «在» New York «要» «開始» «運作» «前» «一個» «月» «告知» you
  5. (8%) [we, 17%] «不著» «急» «、» you «先» «試戴» «量子» «環» «反應» «如何» «在» say/speak «、» I «在» New York «要» «開始» «運作» «前» «一個» «月» «告知» you
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to

### [3/25 10:28 PM]
**Chinese:** 沒關係、等改天搬去就熟悉了、現在還不著急等運作再說吧
**Primary (H=2.32):** [I, 36%] no/not «關» «係» «、» «改天» «搬去» then/just «熟悉» [completed] «、» now still «不著» «急等» «運作» «再» say/speak (let's / how about)
**Alternatives:**
  1. (7%) [I, 36%] no/not «關» «係» «、» «改天» «搬去» then/just «熟悉» [completed] «、» now still «不著» «急等» «運作» «再» say/speak (let's / how about)
  2. (7%) [I, 36%] no/not «關» «係» «、» «改天» «搬去» exactly «熟悉» [completed] «、» now still «不著» «急等» «運作» «再» say/speak (let's / how about)
  3. (7%) [I, 36%] no/not «關» «係» «、» «改天» «搬去» as_soon_as «熟悉» [completed] «、» now still «不著» «急等» «運作» «再» say/speak (let's / how about)
  4. (7%) [I, 36%] no/not «關» «係» «、» «改天» «搬去» only «熟悉» [completed] «、» now still «不著» «急等» «運作» «再» say/speak (let's / how about)
  5. (7%) [I, 36%] no/not «關» «係» «、» «改天» «搬去» then/just «熟悉» [completed] «、» now also «不著» «急等» «運作» «再» say/speak (let's / how about)
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **吧**: suggestion: Let's... / How about..., concession: Fine, go ahead / I suppose so, uncertainty: I think so / probably, softened_command: You should... (softened)
  - polysemy on **就**: then/just: Then/just/simply, exactly: Exactly/precisely, as_soon_as: As soon as, only: Only/merely
  - polysemy on **還**: still: Still/yet, also: Also/in addition, even: Even (more), fairly: Fairly/passably
  - polysemy on **說**: say/speak: To say/speak, scold: To scold/lecture, mean: To mean/refer to

### [3/26 9:33 AM]
**Chinese:** 好的、快去吃早餐吧
**Primary (H=2.32):** [I, 36%] good «、» «快» go eat breakfast (let's / how about)
**Alternatives:**
  1. (15%) [I, 36%] good «、» «快» go eat breakfast (let's / how about)
  2. (15%) [I, 36%] ok/agreed «、» «快» go eat breakfast (let's / how about)
  3. (15%) [I, 36%] good «、» «快» go eat breakfast (fine / I suppose)
  4. (15%) [I, 36%] good «、» «快» go eat breakfast (I think / probably)
  5. (15%) [I, 36%] good «、» «快» go eat breakfast (you should)
**Ambiguities detected:**
  - prodrop on **[dropped subject]**: 我, 你, 我們, 她
  - particle on **吧**: suggestion: Let's... / How about..., concession: Fine, go ahead / I suppose so, uncertainty: I think so / probably, softened_command: You should... (softened)
  - polysemy on **好**: good: Good/fine, ok/agreed: OK/agreed/will do

---
## Section 2: High-Confidence Translations
*Translations where the engine is most certain.*

### 2/20
- None**你好，我是Cindy** → «你好» «，» I is/am/are «Cindy»
- None**你是賈斯丁** → you is/am/are «賈斯丁»
- None**下雨天回去小心慢慢開車** → «下雨天» go back be careful slowly/take your time drive
- [9:47 PM] **那你平常都幾點睡覺？幾點起床** → «那» you «平常» «都» «幾點» sleep «？» «幾點» wake up
### 2/21
- [9:47 PM] **早上好** → good morning
- [9:47 PM] **我在吃早餐** → I «在» eat breakfast
- [9:47 PM] **我已經加你了，請你去通過** → I «已經» «加» you [completed] «，» «請» you go «通過»
- [9:47 PM] **你也這麼早起床** → you «也» «這麼» «早» wake up
- [9:47 PM] **早餐就是木瓜牛奶、水煮蛋牛油果堅果** → breakfast «就是» «木瓜» «牛奶» «、» boiled egg avocado nuts
- [9:41 AM] **我一直都是當會計，因為我在台灣唸書是唸商科的** → I «一直» «都» is/am/are «當» «會計» «，» «因為» I «在» «台» «灣» «唸» «書» is/am/are «唸» «商科»
- [10:13 AM] **她們這裡都是天天上班** → they «這裡» «都» is/am/are «天天» «上班»
- [4:05 PM] **你們這邊我不熟悉，我才來第六天** → you all «這邊» I not «熟悉» «，» I «才» come «第六天»
- [4:10 PM] **你平常都吃什麼** → you «平常» «都» eat «什麼»
- [4:20 PM] **謝謝你的好意、** → thank you you «好意» «、»
- [4:20 PM] **謝謝你的關心、要吃好料，還想到我們、** → thank you you «關心» «、» «要» eat «好料» «，» «還» «想到» we «、»
- [9:03 PM] **她在忙一下** → she «在» busy «一下»
- [9:03 PM] **你先吃晚餐** → you «先» eat dinner
### 2/22
- [1:26 PM] **不要為了這個語言這麼辛苦，你發你方便的我都可以翻譯** → «不要» «為了» «這個» «語言» «這麼» hard/difficult «，» you «發» you «方便» I «都» «可以» «翻譯»
- [3:06 PM] **這樣子很棒、沒有什麼比平安健康最重要** → «這樣» «子» «很棒» «、» don't have «什麼» «比» peace/safe healthy «最» important
- [4:22 PM] **他們這裡是全年無休的** → they «這裡» is/am/are «全年» «無休»
- [4:35 PM] **這是你們美國一個沃倫博士發明的** → «這» is/am/are you all «美國» «一個» «沃倫» «博士» «發明»
- [4:35 PM] **我們台灣的是講國語的，你們美國的是講英文的** → we Taiwan is/am/are «講» «國語» «，» you all «美國» is/am/are «講» «英文»
- [4:35 PM] **所以我都是看台灣的中文字幕** → «所以» I «都» is/am/are «看台» «灣» «中文字幕»
- [5:29 PM] **這個就是博士跟他的女兒去我們台灣** → «這個» «就是» «博士» «跟» he «女兒» go we Taiwan
- [5:54 PM] **我們家爸媽生了七個女生一個弟弟、我是排行第一的、我有六個妹妹一個弟弟、五個妹妹嫁出去、他們五個嫁出去生了總共九個小baby、只有我跟老三沒結婚沒生小孩** → we «家» «爸» «媽» «生» [completed] «七個» «女生» «一個» younger brother «、» I is/am/are «排行» «第一» «、» I have «六個» younger sister «一個» younger brother «、» «五個» younger sister «嫁出去» «、» they «五個» «嫁出去» «生» [completed] «總共» «九個» «小» «baby» «、» «只有» I «跟» «老三» no/not «結婚» no/not «生小孩»
- [9:03 PM] **她在忙一下** → she «在» busy «一下»
- [9:03 PM] **你先吃晚餐** → you «先» eat dinner
### 2/23
- [1:21 PM] **我們的產品是全球統一價錢123美元** → we product is/am/are «全球» «統一» «價錢» «123» «美元»
- [1:34 PM] **你是怎麼受傷？傷的傷在哪裡？** → you is/am/are «怎麼» «受傷» «？» «傷» «傷» «在» «哪裡» «？»
- [1:34 PM] **這個問題明天我幫你問問我們台湾的老師、** → «這個» «問題» tomorrow I help you «問» «問» we «台湾» «老師» «、»
- [1:34 PM] **現在台灣是凌晨三點、等到明天中午我再幫你問看看** → now Taiwan is/am/are «凌晨» «三點» «、» «等到» tomorrow noon I «再» help you «問» «看看»
- [2:14 PM] **這些人帶著都是出來自己見證哪裡的狀況跟大家分享的** → «這些» «人» «帶著» «都» is/am/are «出來» oneself «見證» «哪裡» «狀況» «跟» everyone «分享»
- [2:32 PM] **我們的產品目前缺貨、等有貨了，我再告知、因為很多人在等著，也請你再等等、不著急** → we product «目前» «缺貨» «、» «有貨» [completed] «，» I «再» «告知» «、» «因為» «很多» «人» «在» «等著» «，» «也» «請» you «再» «、» «不著» «急»
- [3:48 PM] **我同事在用午餐跟晚餐了、你吃飽了沒？** → I coworker «在» «用» lunch «跟» dinner [completed] «、» you eat «飽» [completed] no/not «？»
- [3:48 PM] **我同事用的午晚餐** → I coworker «用» «午» dinner
- [3:48 PM] **我也不懂、女生用的** → I «也» not understand «、» «女生» «用»
- [8:15 PM] **我們今天預約了三隊夫妻按摩，現在在忙** → we today «預約» [completed] «三隊» «夫妻» «按摩» «，» now «在» busy
### 2/24
- [11:22 AM] **早上好** → good morning
- [11:22 AM] **謝謝你，你也一樣** → thank you you «，» you «也»
- [12:22 PM] **我們家都沒人抽煙，所以我也不懂、應該會有關係吧、但是還是要多少吃一點、這樣身體才會健康** → we «家» «都» «沒人» «抽煙» «，» «所以» I «也» not understand «、» «應該» «會» have «關» «係» (let's / how about) «、» «但是» «還是» «要» «多少» eat «一點» «、» «這樣» body/health «才» «會» healthy
- [2:21 PM] **你是最棒的、大家一起成長、加油** → you is/am/are «最» great «、» everyone «一起» «成長» «、» keep it up/go for it
### 2/25
- [10:57 AM] **早上好** → good morning
- [10:57 AM] **你也要起來吃早餐** → you «也» «要» «起來» eat breakfast
- [10:57 AM] **謝謝你、快去吃早餐** → thank you you «、» «快» go eat breakfast
- [10:57 AM] **我不喜歡泡腳** → I not like «泡腳»
- [10:57 AM] **你在家可以多泡腳一下** → you «在家» «可以» «多» «泡腳» «一下»
- [10:57 AM] **你先針灸，試看看，等我的產品來再給你試戴看看** → you «先» «針灸» «，» «試» «看看» «，» I product come «再» «給» you «試戴» «看看»
- [12:46 PM] **那真的很棒、出門在外開車注意安全、** → «那» «真的» «很棒» «、» «出門» «在外» drive «注意安全» «、»
- [7:25 PM] **我們現在剛要吃午餐** → we now «剛» «要» eat lunch
- [7:25 PM] **午餐跟晚餐一起吃** → lunch «跟» dinner «一起» eat
- [8:00 PM] **我不怕冷** → I «不怕» «冷»
- [8:00 PM] **我不會我很健康** → I not «會» I «很» healthy
- [8:45 PM] **我們也準備下班了、老闆娘要來接我們回她們家** → we «也» «準備» «下班» [completed] «、» «老» «闆» «娘» «要» come «接» I «們» return/go back she «們» «家»
- [10:43 PM] **晚安** → good night
### 2/26
- [8:02 AM] **早上好** → good morning
- [8:02 AM] **我沒有那麼早睡、我下班回來都會跟我爸爸媽媽他們聊天** → I don't have «那麼» «早睡» «、» I «下班» come back «都» «會» «跟» I dad mom they «聊天»
- [11:09 AM] **我的早餐** → I breakfast
- [11:09 AM] **謝謝你，你們也要一樣一起大家都吃早餐** → thank you you «，» you all «也» «要» «一起» everyone «都» eat breakfast
- [11:09 AM] **對、很乖** → right/correct «、» «很乖»
- [4:19 PM] **我的台灣名字是** → I Taiwan «名字» is/am/are
- [4:19 PM] **全球吸引力產品** → «全球» «吸引力» product
- [4:19 PM] **我會有名片** → I «會» have «名片»
- [6:01 PM] **英文名字** → «英文名字»
- [6:01 PM] **你的家人住哪裡？** → you family live «哪裡» «？»
- [6:01 PM] **水煮的午餐跟晚餐** → water cook lunch «跟» dinner
- [6:01 PM] **現在的社會很現實、我們能吃要平安健康就是財富** → now «社會» «很» «現實» «、» we «能» eat «要» peace/safe healthy «就是» «財富»
- [6:01 PM] **你們美國人都是用叉子跟刀子** → you all «美國» «人» «都» is/am/are «用» «叉子» «跟» «刀子»
- [6:01 PM] **很棒** → «很棒»
- [9:38 PM] **我是家族里最笨的一個、所以我才跟老三、一樣不結婚、我們倆一直都單身** → I is/am/are «家族» «里» «最笨» «一個» «、» «所以» I «才» «跟» «老三» «、» «一樣» not «結婚» «、» we «倆» «一直» «都» «單身»
- [10:58 PM] **晚安** → good night
### 2/27
- [12:17 PM] **對** → right/correct
- [1:29 PM] **現在的時機不要亂投資，把錢放身上是最安全的** → now «時機» «不要» «亂» «投資» «，» «把» money «放» «身上» is/am/are «最» safety/safe
- [4:19 PM] **對** → right/correct
- [4:19 PM] **棒棒** → «棒棒»
- [4:19 PM] **你去找吃的** → you go «找» eat
- [5:45 PM] **很棒** → «很棒»
### 2/28
- [7:59 AM] **早上好** → good morning
- [7:59 AM] **我也剛剛起床、刷牙洗臉等等8:50會去公司、我們這裡是九點上到晚上九點** → I «也» «剛剛» wake up «、» «刷牙» «洗» «臉» «8» «:» «50» «會去» company «、» we «這裡» is/am/are «九點» «上到» evening «九點»
- [9:23 AM] **雞蛋最好要吃熟的、因為現在全世界病毒都很多、吃熟的對身體好沒細菌** → «雞蛋» «最好» «要» «吃熟» «、» «因為» now «全世界» «病毒» «都» «很多» «、» «吃熟» «對身體好» «沒細菌»
- [10:04 AM] **我跟另一女孩的早餐** → I «跟» «另» «一» «女孩» breakfast
- [10:04 AM] **早餐簡單的是我負責、** → breakfast simple is/am/are I «負責» «、»
- [10:04 AM] **午餐跟晚餐是另外一個女孩或者老闆娘負責** → lunch «跟» dinner is/am/are «另外» «一個» «女孩» «或者» «老» «闆» «娘» «負» «責»
- [10:04 AM] **因為我不會做菜，我只會用簡單的、所以早餐我負責午餐晚餐，他們兩個會用好料好吃的** → «因為» I not «會» «做菜» «，» I «只» «會» «用» simple «、» «所以» breakfast I «負責» lunch dinner «，» they «兩個» «會» «用» «好料» «好吃»
- [10:04 AM] **你看錯了、我們的早餐一定有牛油果跟水煮蛋蛋、其他肯定是老闆娘或女孩用的、** → you «看錯» [completed] «、» we breakfast «一定» have avocado «跟» boiled egg «蛋» «、» «其他» «肯定» is/am/are «老» «闆» «娘» «或» «女孩» «用» «、»
- [10:04 AM] **只有牛油果跟水煮蛋的部分才是早餐、** → «只有» avocado «跟» boiled egg «部分» «才» is/am/are breakfast «、»
- [3:15 PM] **雞蛋大顆的煮法、水滾了放下去煮10分鐘、取出來泡冷水、** → «雞蛋» «大顆» «煮法» «、» water «滾» [completed] «放下去» cook «10» «分鐘» «、» «取出» come «泡» «冷水» «、»
- [3:15 PM] **雞蛋小顆的煮法、水滾了放下去煮8分鐘、取出來泡冷水** → «雞蛋» «小» «顆» «煮法» «、» water «滾» [completed] «放下去» cook «8» «分鐘» «、» «取出» come «泡» «冷水»
- [3:15 PM] **我們今天的午餐跟晚餐** → we today lunch «跟» dinner
- [8:14 PM] **我們家人不是客家人** → we family «不是» «客家人»
- [8:14 PM] **我們是純屬的正宗台灣人** → we is/am/are «純屬» «正宗» Taiwan «人»
### 3/1
- [12:08 PM] **我在台灣是唸商科的** → I «在» Taiwan is/am/are «唸» «商科»
- [12:08 PM] **在學校唸了三年會計科** → «在» «學校» «三年» «會» «計科»
- [2:31 PM] **哈哈** → «哈哈»
- [2:41 PM] **每天吃不一樣的也很棒** → «每天» eat not «也» «很棒»
- [2:41 PM] **我不喝酒也不抽煙** → I not «喝酒» «也» not «抽煙»
- [6:56 PM] **對** → right/correct
### 3/2
- [11:16 AM] **我們的早餐** → we breakfast
- [11:33 AM] **昨天老闆娘去沃爾瑪買的** → yesterday «老» «闆» «娘» go «沃» «爾» «瑪» buy
- [11:33 AM] **那改天我們的產品來了，你可以帶紫色的、每個顏色每個顏色的功效紫色是放鬆幫助睡眠的** → «那» «改天» we product come [completed] «，» you «可以» bring/wear «紫色» «、» «每個» «顏色» «每個» «顏色» «功效» «紫色» is/am/are «放» «鬆» help «助» «睡眠»
- [12:02 PM] **公司保險理賠、一次付款或分次付款** → company «保險» «理賠» «、» «一次» «付款» «或» «分次» «付款»
- [7:36 PM] **我要去放錢進去，因為報稅的錢從卡片扣** → I «要» go «放錢» «進去» «，» «因為» «報稅» money «從» «卡片» «扣»
- [7:57 PM] **哈哈** → «哈哈»
- [7:57 PM] **對** → right/correct
- [7:57 PM] **你平常這麼早睡這麼乖** → you «平常» «這麼» «早睡» «這麼» well-behaved/good
### 3/3
- [8:25 AM] **早上好** → good morning
- [8:25 AM] **台灣的元宵節** → Taiwan «元宵» «節»
- [8:25 AM] **台灣跟大陸的正月十五元宵節** → Taiwan «跟» «大陸» «正月十五» «元宵» «節»
- [8:25 AM] **哈哈** → «哈哈»
- [10:51 AM] **我們的早餐** → we breakfast
- [10:51 AM] **紅豆、山藥、紅棗、黑芝麻湯圓、花生湯圓、小米粥、** → «紅豆» «、» «山藥» «、» «紅棗» «、» «黑芝麻» «湯圓» «、» «花生» «湯圓» «、» «小米粥» «、»
- [10:51 AM] **水煮蛋、牛油果** → boiled egg «、» avocado
- [11:59 AM] **稻米** → «稻米»
- [11:59 AM] **時間** → time
- [6:57 PM] **這樣子不多一點點而已** → «這樣» «子» not «多» «一» «點» «點»
- [8:51 PM] **這個是我們的晚餐** → «這個» is/am/are we dinner
### 3/4
- [9:18 AM] **早上好** → good morning
- [10:34 AM] **哈哈** → «哈哈»
- [1:11 PM] **你那個是葡萄、鳳梨、水煮蛋** → you «那個» is/am/are «葡萄» «、» «鳳梨» «、» boiled egg
- [1:11 PM] **我們每天都會吃水煮蛋** → we «每天» «都» «會» eat boiled egg
- [5:14 PM] **棒棒為了健康加油** → «棒棒» «為了» healthy keep it up/go for it
- [8:27 PM] **我們的晚餐** → we dinner
- [8:27 PM] **你這個裡面有加蘑菇，我有看到** → you «這個» «裡面» «有加» «蘑菇» «，» I have «看到»
- [8:27 PM] **最好不要常喝可樂對身體不好、喝白開水最好** → «最好» «不要» «常喝» «可樂» right/correct body/health «不好» «、» «喝白» «開水» «最好»
### 3/5
- [11:11 AM] **你的也很棒** → you «也» «很棒»
- [5:27 PM] **今天我們吃素食、這些都是水煮的** → today we eat «素食» «、» «這些» «都» is/am/are water cook
### 3/6
- [2:30 PM] **不一樣，你的是你自己製作的規劃、我的是公司的** → not «，» you is/am/are you oneself «製» «作» «規» «劃» «、» I is/am/are company
- [9:33 PM] **你也要早點睡別太累晚安安** → you «也» «要» «早點» «睡別» «太» «累» good night «安»
### 3/7
- [8:46 AM] **早上好** → good morning
- [12:40 PM] **所以我們要大家要珍惜當下的平安健康** → «所以» we «要» everyone «要» «珍惜» «當下» peace/safe healthy
- [1:45 PM] **對** → right/correct
- [10:14 PM] **晚安** → good night
### 3/8
- [10:42 AM] **早餐** → breakfast
- [10:42 AM] **你也快點去吃** → you «也» «快點» go eat
- [11:24 AM] **那你那個我們台湾叫斷食法** → «那» you «那個» we «台湾» «叫斷» «食法»
- [11:50 AM] **早餐我們都吃得簡單不吃米飯、除非我有煮小米南瓜粥、或者小米山藥粥** → breakfast we «都» eat simple «不吃» «米» rice/meal «、» «除非» I have cook «小米» «南瓜» «粥» «、» «或者» «小米» «山藥» «粥»
- [12:52 PM] **我先去忙** → I «先» go busy
- [5:58 PM] **這個是我們今天三八女神節，我同事用的** → «這個» is/am/are we today «三八» «女神» «節» «，» I coworker «用»
- [8:56 PM] **哈哈** → «哈哈»
- [8:56 PM] **那你早點睡，晚安** → «那» you «早點» «睡» «，» good night
### 3/9
- [9:33 AM] **你今天是斷食第二天了，多喝溫開水加油** → you today is/am/are «斷» «食» «第二天» [completed] «，» «多» drink «溫開水» keep it up/go for it
- [12:29 PM] **台灣歌星、蔡幸娟、** → Taiwan «歌星» «、» «蔡幸娟» «、»
- [3:14 PM] **那很棒** → «那» «很棒»
- [7:42 PM] **我們也剛剛吃飯** → we «也» «剛剛» eat rice/meal
### 3/10
- [6:17 PM] **我們剛剛忙好、同事在煮菜** → we «剛剛» «忙好» «、» coworker «在» «煮菜»
- [6:17 PM] **空腹三天後、只能吃流質湯湯水水、不可以吃太多東西，不然胃會受不了** → «空腹» «三天» «後» «、» «只能» eat «流質» «湯» «湯» «水水» «、» not «可以» eat «太多東西» «，» «不然» «胃會» «受不了»
- [9:10 PM] **哈哈** → «哈哈»
### 3/11
- [4:25 PM] **你要多吃一些流質的食物** → you «要» «多» eat «一些» «流質» «食物»
- [6:49 PM] **我們的** → we
- [7:31 PM] **甜椒** → «甜椒»
- [7:31 PM] **甜椒，對身體健康也好** → «甜椒» «，» right/correct body/health healthy
- [9:36 PM] **晚安** → good night
### 3/12
- [11:13 AM] **那你很棒** → «那» you «很棒»
- [11:59 AM] **我不懂麻將，因為我們家都不會玩** → I not understand «麻» «將» «，» «因為» we «家» «都» not «會» «玩»
- [4:59 PM] **我們的晚餐** → we dinner
- [9:32 PM] **你也很棒** → you «也» «很棒»
### 3/13
- [10:04 AM] **早上好** → good morning
- [11:23 AM] **熱美式咖啡一杯多少錢** → «熱» «美式» «咖啡» «一杯» «多少» money
- [12:18 PM] **每日喝一杯** → «每日» «喝一杯»
- [12:18 PM] **自己泡的咖啡** → oneself «泡» «咖啡»
- [10:00 PM] **晚安** → good night
### 3/14
- [2:28 PM] **我不曾過情人節、因為我沒結婚也沒交男朋友** → I «不曾» «情人» «節» «、» «因為» I no/not «結婚» «也» «沒交» «男朋友»
- [2:28 PM] **所以我也不懂懂這個、沒關係，大家都是朋友這個不拘小節，謝謝你** → «所以» I «也» not understand understand «這個» «、» no/not «關» «係» «，» everyone «都» is/am/are friend «這個» «不拘» «小節» «，» thank you you
- [4:14 PM] **哈哈** → «哈哈»
- [9:49 PM] **我們家都不吃生魚片之類、還有生的東西我們家也都不吃、那裡面很多細菌我們看不到** → we «家» «都» «不吃» «生魚» «片» «之類» «、» «還» «有生» «東西» we «家» «也» «都» «不吃» «、» «那裡» «面» «很多» «細菌» we «看不到»
- [9:49 PM] **生魚片或者是魚類的食物、我們都是會煮熟才吃** → «生魚» «片» «或者» is/am/are «魚類» «食物» «、» we «都» is/am/are «會» «煮熟» «才» eat
- [9:49 PM] **晚安** → good night
### 3/15
- [9:08 AM] **早上好** → good morning
- [10:06 AM] **我們今天早上來一對夫妻按摩** → we today morning come «一對» «夫妻» «按摩»
- [11:48 AM] **我很少看電視** → I «很少» «看電視»
- [7:36 PM] **味噌鮭魚豆腐湯** → «味» «噌» «鮭魚» «豆腐» «湯»
- [10:39 PM] **晚安** → good night
### 3/16
- [2:16 PM] **什麼跟工作有關的？** → «什麼» «跟» work «有關» «？»
### 3/17
- [8:40 AM] **早上好** → good morning
- [8:40 AM] **你也是** → you «也» is/am/are
### 3/18
- [9:35 AM] **早上好** → good morning
- [9:57 PM] **很美、謝謝你、晚安** → «很» «美» «、» thank you you «、» good night
### 3/19
- [9:01 AM] **早上好** → good morning
- [10:56 AM] **大家平平安安健健康康** → everyone «平平安安» «健健康康»
- [10:56 AM] **農曆2月2號** → «農» «曆» «2» «月» «2» «號»
- [10:56 AM] **將頭髮剪一些** → «將» «頭» «髮» «剪» «一些»
- [10:56 AM] **代表不好的運氣剪掉** → «代表» «不好» «運氣» «剪掉»
- [10:56 AM] **你明天要來我們店按摩、** → you tomorrow «要來» we «店» «按摩» «、»
- [10:56 AM] **你現在沒在工作，不要浪費錢，把錢存起來、** → you now no/not «在» work «，» «不要» «浪費錢» «，» «把» money «存起» come «、»
- [11:15 AM] **我看不懂你的意思** → I «看不懂» you «意思»
- [11:15 AM] **你現在沒工作，最主要是存錢、用應該用的、發該發的** → you now no/not work «，» «最» «主要» is/am/are «存錢» «、» «用» «應該» «用» «、» «發該» «發»
- [11:38 AM] **可以自己評估、錢要分散來投資、不要只有當一個投資、避免風險** → «可以» oneself «評估» «、» money «要» «分散» come «投資» «、» «不要» «只有» «當» «一個» «投資» «、» «避免» «風險»
- [12:00 PM] **你們美國人、跟我們台灣人不一樣、你們這裡的人都不像你這麼乖會存錢** → you all «美國» «人» «、» «跟» we Taiwan «人» not «、» you all «這裡» «人» «都» not «像» you «這麼» «乖會» «存錢»
- [12:21 PM] **所以你的家裡成員** → «所以» you «家裡» «成員»
- [12:21 PM] **那可能很難、我周圍沒有這種人、** → «那» «可能» «很» «難» «、» I «周圍» don't have «這種» «人» «、»
- [12:21 PM] **這個是去百度查你的生肖屬老鼠** → «這個» is/am/are go «百度» «查» you «生肖» «屬» «老鼠»
- [12:21 PM] **你的另一半適合老鼠、猴子、龍** → you «另一半» «適合» «老鼠» «、» «猴子» «、» «龍»
- [1:31 PM] **晚點再聊天** → «晚點» «再» «聊天»
- [6:28 PM] **哈哈、韓國字我也不懂** → «哈哈» «、» «韓國» «字» I «也» not understand
- [6:28 PM] **你回去了嗎？吃晚餐了沒？** → you go back [completed] «？» eat dinner [completed] no/not «？»
- [6:28 PM] **你的爸爸是軍人、那你怎麼不是** → you dad is/am/are «軍人» «、» «那» you «怎麼» «不是»
- [6:28 PM] **那是白菜** → «那» is/am/are «白菜»
- [9:57 PM] **我是小狗、生日8月1日吉時生** → I is/am/are «小狗» «、» «生日» «8» «月» «1» «日吉» «時生»
- [10:15 PM] **晚安** → good night
### 3/20
- [9:40 AM] **對** → right/correct
- [10:55 AM] **我在鄉村長大、在城市上課跟工讀生** → I «在» «鄉村» «長大» «、» «在» «城市» «上課» «跟» «工讀» «生»
- [10:55 AM] **我的爸媽很偉大、生我們七個女生一個男生、很辛苦的把我們養大、所以我們都要孝順父母、** → I «爸媽» «很» «偉大» «、» «生» we «七個» «女生» «一個» «男生» «、» «很» hard/difficult «把» we «養» «大» «、» «所以» we «都» «要» «孝順» «父母» «、»
- [11:31 AM] **等我回紐約、開始做量孑環的產品、認真賺錢快一點回台灣陪爸媽** → I return/go back New York «、» «開始» «做量» «孑環» product «、» «認真» «賺» money «快» «一點» return/go back Taiwan «陪» «爸媽»
- [11:31 AM] **我們回去紐約告知你** → we go back New York «告知» you
- [12:19 PM] **我來這裡學習按摩、只是過來幫另一個女孩的忙、因為另一個女孩回大陸陪家人** → I come «這裡» study/learn «按摩» «、» «只是» «過來» help «另» «一個» «女孩» «的忙» «、» «因為» «另» «一個» «女孩» «回大陸» «陪» family
- [12:19 PM] **所有美國的按摩院、都不是團隊、都是個人應徵工作的、** → «所有» «美國» «按摩院» «、» «都» «不是» «團隊» «、» «都» is/am/are «個» «人» «應徵» work «、»
- [2:23 PM] **聊天就是無所不聊** → «聊天» «就是» «無所不聊»
- [2:43 PM] **我們的午晚餐** → we «午» dinner
- [4:57 PM] **我的是長髮** → I is/am/are «長» «髮»
- [4:57 PM] **我的長** → I «長»
- [8:37 PM] **這個是紐約、我跟另一個女孩我們兩個人一起租的三房二廳兩個衛浴設備** → «這個» is/am/are New York «、» I «跟» «另» «一個» «女孩» we «兩個» «人» «一起» rent «三房» «二» «廳» «兩個» «衛浴» «設備»
- [8:37 PM] **這個也是台灣的代購群，請我幫她買的衣服跟包包** → «這個» «也» is/am/are Taiwan «代購» «群» «，» «請» I help she buy «衣服» «跟» «包包»
- [8:37 PM] **等你去紐約，我再請你喝** → you go New York «，» I «再» «請» you drink
- [8:37 PM] **以後有機會你搬去紐約** → «以» «後» have «機會» you «搬去» New York
- [8:37 PM] **現金** → «現金»
- [8:37 PM] **為什麼要熬夜？** → «為» «什麼» «要» «熬夜» «？»
### 3/21
- [10:00 AM] **這是雅培桉素牛奶加燕窩** → «這» is/am/are «雅培» «桉素» «牛奶» «加燕» «窩»
- [10:00 AM] **早餐只要自己喜歡吃吃什麼都可以** → breakfast «只要» oneself like eat eat «什麼» «都» «可以»
- [10:00 AM] **午餐晚餐、盡量能晚上六點前吃完、對身體最好** → lunch dinner «、» «盡量» «能» evening «六點» «前» eat «完» «、» right/correct body/health «最好»
- [11:59 AM] **你那麼晚睡、可以晚一點吃午餐跟晚餐、** → you «那麼» «晚睡» «、» «可以» «晚» «一點» eat lunch «跟» dinner «、»
- [7:32 PM] **我的午晚餐** → I «午» dinner
- [8:23 PM] **台灣有賣** → Taiwan have sell
- [9:09 PM] **對** → right/correct
- [9:09 PM] **你也早點休息** → you «也» «早點» «休息»
### 3/22
- [7:11 PM] **你這個披薩這麼多要用保鮮膜一個一個包起來、冰在冷凍要吃再拿下來打熱** → you «這個» «披薩» «這麼» «多要» «用» «保鮮» «膜» «一個» «一個» «包起» come «、» «冰在» «冷凍» «要» eat «再» «拿下» come «打熱»
- [7:11 PM] **對** → right/correct
- [9:02 PM] **我家的荔枝超級的多、有很多種不一樣的品種** → «我家» «荔枝» «超級» «多» «、» have «很多» «種» not «品種»
- [10:24 PM] **晚安** → good night
### 3/23
- [10:41 AM] **下雨天肯定是陰天** → «下雨天» «肯定» is/am/are «陰天»
- [11:02 AM] **台灣跟大陸都會通** → Taiwan «跟» «大陸» «都» «會» «通»
- [12:06 PM] **棒** → great
- [7:04 PM] **牛榜** → «牛榜»
- [7:04 PM] **我們的是牛蒡雞腳湯** → we is/am/are «牛蒡» «雞» «腳» «湯»
### 3/24
- [9:10 AM] **早上好** → good morning
- [9:10 AM] **我們正在吃早餐** → we «正在» eat breakfast
- [9:10 AM] **山藥小米粥、牛油果、水煮蛋、堅果** → «山藥» «小米粥» «、» avocado «、» boiled egg «、» nuts
- [9:10 AM] **水煮蛋要每天吃二個、** → boiled egg «要» «每天» eat «二個» «、»
- [9:10 AM] **蛋白質很重要** → «蛋白» «質» «很» important
- [9:36 AM] **很乖** → «很乖»
- [9:36 AM] **水煮蛋可以每天吃二個、水果可以中午在吃、因為冷的食物** → boiled egg «可以» «每天» eat «二個» «、» «水果» «可以» noon «在» eat «、» «因為» «冷» «食物»
- [10:23 AM] **水果是冷的食物、最好不要空腹吃** → «水果» is/am/are «冷» «食物» «、» «最好» «不要» «空腹吃»
- [10:23 AM] **不是工廠、** → «不是» «工廠» «、»
- [10:23 AM] **我先去忙** → I «先» go busy
- [11:22 AM] **嗨** → «嗨»
- [11:22 AM] **3月28日、3月29日、3月30日、3月31日、** → «3» «月» «28» «日» «、» «3» «月» «29» «日» «、» «3» «月» «30» «日» «、» «3» «月» «31» «日» «、»
- [11:22 AM] **我請你吃飯、** → I «請» you eat rice/meal «、»
- [11:22 AM] **你這裡去法拉盛好像是三個半小時** → you «這裡» go «法拉盛» «好像» is/am/are «三個半» «小» «時»
- [11:34 AM] **我有叫一個搬家公司了、因為那個房間的床、跟沙發我都都不會拆、我也搬不動** → I have «叫» «一個» «搬家» company [completed] «、» «因為» «那個» «房間» «床» «、» «跟» «沙發» I «都» «都» not «會» «拆» «、» I «也» move «不動»
- [11:34 AM] **你去法拉盛、我在介紹你去針灸、法拉盛的針灸很厲害、不像外州的不專業** → you go «法拉盛» «、» I «在» «介紹» you go «針灸» «、» «法拉盛» «針灸» «很» impressive «、» not «像» «外州» not «專業»
- [11:34 AM] **你們這裡的針灸，不像法拉盛那麼專業** → you all «這裡» «針灸» «，» not «像» «法拉盛» «那麼» «專業»
- [11:34 AM] **我也是穿T恤跟牛仔褲** → I «也» is/am/are «穿» «T恤» «跟» «牛仔» «褲»
- [11:34 AM] **因為那四天，只有姐姐，他們那一對夫妻、沒有其他的、因為大家都在工作上那四天沒有空跟你碰面、要等下一次有機會大家都回去、才會請你跟他們碰面** → «因為» «那» «四天» «，» «只有» «姐姐» «，» they «那一» right/correct «夫妻» «、» don't have «其他» «、» «因為» everyone «都» «在» work «上» «那» «四天» no/not «有空» «跟» you «碰面» «、» «要» «下» «一次» have «機會» everyone «都» go back «、» «才» «會» «請» you «跟» they «碰面»
- [11:34 AM] **我先去忙** → I «先» go busy
- [1:24 PM] **什麼是潛規則？聽不懂？** → «什麼» is/am/are «潛» «規則» «？» «聽» not understand «？»
- [1:24 PM] **我認識的朋友、都很好相處、沒有那麼多講究** → I know/meet friend «、» «都» «很好» «相處» «、» don't have «那麼» «多» «講究»
- [2:02 PM] **這個老奶奶現在身體指數全部都在改善** → «這個» «老奶奶» now body/health «指數» «全部» «都» «在» improve
- [2:02 PM] **大家都知道的道理** → everyone «都» know «道理»
- [2:22 PM] **什麼是藏品散落各地、聽不懂？** → «什麼» is/am/are «藏品» «散落» «各地» «、» «聽» not understand «？»
- [7:02 PM] **很好的晚餐** → «很好» dinner
- [7:54 PM] **你現在在哪個州吃飯？** → you now «在» «哪個» «州» eat rice/meal «？»
- [9:24 PM] **小心開車、沒事** → be careful drive «、» it's nothing/no problem
- [9:36 PM] **我們27號下午回纽约、** → we «27» «號» «下午» return/go back «纽约» «、»
- [9:36 PM] **你3月28日去紐約找我們** → you «3» «月» «28» «日去» New York «找» we
- [9:36 PM] **你有空去看看，我之前Po給你的英文的版面、介紹我們量子環的產品的功效** → you «有空» go «看看» «，» I «之前» «Po» «給» you «英文» «版面» «、» «介紹» we «量子» «環» product «功效»
- [10:40 PM] **我很歡迎你在紐約跟我們一起吃飯** → I «很» «歡迎» you «在» New York «跟» we «一起» eat rice/meal
- [10:40 PM] **你現在的身體狀況、在紐約工作對你是最方便的、可以每天有現金收入、又可以不會太累的工作、** → you now body/health «狀況» «、» «在» New York work right/correct you is/am/are «最» «方便» «、» «可以» «每天» have «現金» «收入» «、» «又» «可以» not «會» «太» «累» work «、»
- [10:40 PM] **我在跟爸爸聊天** → I «在» «跟» dad «聊天»
- [11:15 PM] **爸爸前陣子、忽然跌倒、掛急診** → dad «前» «陣子» «、» «忽然» «跌倒» «、» «掛» «急» «診»
- [11:15 PM] **一個禮拜要去電療五天** → «一個» «禮» «拜» «要» go «電療» «五天»
- [11:15 PM] **我家有拜神明** → «我家» have «拜» «神明»
- [11:15 PM] **觀音菩薩、媽祖娘娘、衆神明** → «觀音» «菩薩» «、» «媽祖» «娘娘» «、» «衆» «神明»
- [11:15 PM] **快十二點了、我要去睡了、晚安** → «快» «十二» «點» [completed] «、» I «要» go «睡» [completed] «、» good night
### 3/25
- [3:00 PM] **你慢慢開車、** → you slowly/take your time drive «、»
- [3:00 PM] **不客氣** → not «客氣»
- [7:54 PM] **為什麼你要租房子？** → «為» «什麼» you «要» «租房子» «？»
- [10:28 PM] **這是在賓州** → «這» is/am/are «在» «賓州»
- [10:28 PM] **晚安** → good night

---
## Section 3: Low-Confidence Translations (1.0 ≤ H < 2.0)
*Two or three competitive interpretations.*

### 2/20
**[2/20 None] 很開心認識你。** (H=1.85)
  Primary: [I, 36%] «很» happy know/meet you «。»
  Alt (36%): [you, 36%] «很» happy know/meet you «。»
  Alt (22%): [we, 22%] «很» happy know/meet you «。»

**[2/20 None] 好的，小心慢慢開車** (H=1.00)
  Primary: good «，» be careful slowly/take your time drive
  Alt (50%): ok/agreed «，» be careful slowly/take your time drive

**[2/20 9:47 PM] 我們下班回來老闆娘他們家了** (H=1.58)
  Primary: we «下班» come back «老» «闆» «娘» he «們» «家» [completed]
  Alt (32%): we «下班» come back «老» «闆» «娘» he «們» «家» [now/changed]
  Alt (32%): we «下班» come back «老» «闆» «娘» he «們» «家» (too much)

### 2/21
**[2/21 9:31 AM] 好厲害** (H=1.00)
  Primary: good impressive
  Alt (50%): ok/agreed impressive

**[2/21 9:49 AM] 上數學課程很好、可以動動頭腦** (H=1.00)
  Primary: «上» «數學» «課程» «很» good «、» «可以» «動動頭» «腦»
  Alt (50%): «上» «數學» «課程» «很» ok/agreed «、» «可以» «動動頭» «腦»

**[2/21 10:13 AM] 是的、我們很幸運** (H=1.85)
  Primary: [you, 37%] is/am/are «、» we «很» «幸運»
  Alt (36%): [I, 36%] is/am/are «、» we «很» «幸運»
  Alt (21%): [we, 21%] is/am/are «、» we «很» «幸運»

**[2/21 10:13 AM] 這裡是9:00到9:00下班** (H=1.00)
  Primary: «這裡» is/am/are «9» «:» «00» arrive «9» «:» «00» «下班»
  Alt (50%): «這裡» is/am/are «9» «:» «00» succeed «9» «:» «00» «下班»

**[2/21 10:13 AM] 你去弄早餐吃吧，我去幫忙打掃衛生** (H=1.58)
  Primary: you go do/handle breakfast eat (let's / how about) «，» I go help busy «打掃» «衛生»
  Alt (33%): you go make/prepare breakfast eat (let's / how about) «，» I go help busy «打掃» «衛生»
  Alt (33%): you go mess_up breakfast eat (let's / how about) «，» I go help busy «打掃» «衛生»

**[2/21 10:13 AM] 是的我生肖屬小狗** (H=1.85)
  Primary: [you, 37%] is/am/are I «生肖» «屬» «小狗»
  Alt (36%): [I, 36%] is/am/are I «生肖» «屬» «小狗»
  Alt (21%): [we, 21%] is/am/are I «生肖» «屬» «小狗»

**[2/21 4:20 PM] 好的** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[2/21 4:20 PM] 我們一天只吃了兩餐、早餐吃了、現在在吃午餐跟晚餐了** (H=1.58)
  Primary: we «一天» «只» eat [completed] «兩餐» «、» breakfast eat [completed] «、» now «在» eat lunch «跟» dinner [completed]
  Alt (32%): we «一天» «只» eat [now/changed] «兩餐» «、» breakfast eat [now/changed] «、» now «在» eat lunch «跟» dinner [now/changed]
  Alt (32%): we «一天» «只» eat (too much) «兩餐» «、» breakfast eat (too much) «、» now «在» eat lunch «跟» dinner (too much)

**[2/21 4:20 PM] 老闆娘不喜歡客人帶東西給員工吃** (H=1.58)
  Primary: «老» «闆» «娘» not «喜» «歡» «客人» bring «東西» «給» «員工» eat
  Alt (33%): «老» «闆» «娘» not «喜» «歡» «客人» wear «東西» «給» «員工» eat
  Alt (33%): «老» «闆» «娘» not «喜» «歡» «客人» lead/guide «東西» «給» «員工» eat

**[2/21 4:20 PM] 你快去吃飯吧** (H=2.00)
  Primary: you «快» go eat rice/meal (let's / how about)
  Alt (25%): you «快» go eat rice/meal (fine / I suppose)
  Alt (25%): you «快» go eat rice/meal (I think / probably)

**[2/21 4:20 PM] 好的** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[2/21 9:03 PM] 我們要回老闆娘家了** (H=1.58)
  Primary: we «要» return/go back «老» «闆» «娘家» [completed]
  Alt (32%): we «要» return/go back «老» «闆» «娘家» [now/changed]
  Alt (32%): we «要» return/go back «老» «闆» «娘家» (too much)

### 2/22
**[2/22 11:47 AM] 謝謝你的關心、下雪天盡量也不要亂跑，你自己也要出門注意安全** (H=1.58)
  Primary: thank you you «關心» «、» «下雪天» «盡量» «也» «不要» «亂» run «，» you oneself «也» «要» «出門» «注意安全»
  Alt (33%): thank you you «關心» «、» «下雪天» «盡量» «也» «不要» «亂» go/visit «，» you oneself «也» «要» «出門» «注意安全»
  Alt (33%): thank you you «關心» «、» «下雪天» «盡量» «也» «不要» «亂» flee «，» you oneself «也» «要» «出門» «注意安全»

**[2/22 1:26 PM] 中午好** (H=1.00)
  Primary: noon good
  Alt (50%): noon ok/agreed

**[2/22 4:35 PM] 學習英文** (H=1.72)
  Primary: [I, 50%] study/learn «英文»
  Alt (28%): [we, 28%] study/learn «英文»
  Alt (16%): [you, 16%] study/learn «英文»

**[2/22 4:35 PM] 有機會你進去看看真的很不錯那個英文我看不懂都要翻譯** (H=1.67)
  Primary: [you, 56%] have «機會» you «進去» «看看» «真的» «很» «不錯» «那個» «英文» I «看不懂» «都» «要» «翻譯»
  Alt (22%): [I, 22%] have «機會» you «進去» «看看» «真的» «很» «不錯» «那個» «英文» I «看不懂» «都» «要» «翻譯»
  Alt (17%): [we, 17%] have «機會» you «進去» «看看» «真的» «很» «不錯» «那個» «英文» I «看不懂» «都» «要» «翻譯»

**[2/22 5:29 PM] 對啊，這個產品、連醫生護士都認可的產品、肯定是不錯的、尤其你們美國人對這些戴在身上的東西都不能接受、那對醫生的病患都能接受證明這些東西是好的** (H=1.00)
  Primary: right/correct ! «，» «這個» product «、» «醫生護士» «都» «認可» product «、» «肯定» is/am/are «不錯» «、» «尤其» you all «美國» «人» right/correct «這些» wear «在» «身上» «東西» «都» «不能» «接受» «、» «那» right/correct «醫生» «病患» «都» «能» «接受» «證明» «這些» «東西» is/am/are good
  Alt (50%): right/correct ! «，» «這個» product «、» «醫生護士» «都» «認可» product «、» «肯定» is/am/are «不錯» «、» «尤其» you all «美國» «人» right/correct «這些» wear «在» «身上» «東西» «都» «不能» «接受» «、» «那» right/correct «醫生» «病患» «都» «能» «接受» «證明» «這些» «東西» is/am/are ok/agreed

**[2/22 5:29 PM] 這個圖就是發明這個量子環的沃倫博士，他得了諾貝爾獎** (H=1.58)
  Primary: «這個» «圖» «就是» «發明» «這個» «量子» «環» «沃倫» «博士» «，» he [completed] «諾貝爾獎»
  Alt (32%): «這個» «圖» «就是» «發明» «這個» «量子» «環» «沃倫» «博士» «，» he [now/changed] «諾貝爾獎»
  Alt (32%): «這個» «圖» «就是» «發明» «這個» «量子» «環» «沃倫» «博士» «，» he (too much) «諾貝爾獎»

**[2/22 5:29 PM] 這個就是這個產品的功效好處** (H=1.00)
  Primary: «這個» «就是» «這個» product «功效» good «處»
  Alt (50%): «這個» «就是» «這個» product «功效» ok/agreed «處»

**[2/22 5:29 PM] 這三張就是我去到哪也都有帶著產品** (H=1.00)
  Primary: «這» «三張» «就是» I go arrive «哪» «也» «都» have «帶著» product
  Alt (50%): «這» «三張» «就是» I go succeed «哪» «也» «都» have «帶著» product

**[2/22 5:29 PM] 這個也是美國人自己帶出來分享的拍的照片** (H=1.58)
  Primary: «這個» «也» is/am/are «美國» «人» oneself bring «出來» «分享» «拍» «照片»
  Alt (33%): «這個» «也» is/am/are «美國» «人» oneself wear «出來» «分享» «拍» «照片»
  Alt (33%): «這個» «也» is/am/are «美國» «人» oneself lead/guide «出來» «分享» «拍» «照片»

**[2/22 5:54 PM] 所以我才要在纽约做這種產品、這樣可以以賺錢貼補家人** (H=1.58)
  Primary: «所以» I «才» «要» «在» «纽约» do/make «這種» product «、» «這樣» «可以» «以» «賺» money «貼補» family
  Alt (33%): «所以» I «才» «要» «在» «纽约» work_as «這種» product «、» «這樣» «可以» «以» «賺» money «貼補» family
  Alt (33%): «所以» I «才» «要» «在» «纽约» conduct «這種» product «、» «這樣» «可以» «以» «賺» money «貼補» family

**[2/22 9:03 PM] 我們要回老闆娘家了** (H=1.58)
  Primary: we «要» return/go back «老» «闆» «娘家» [completed]
  Alt (32%): we «要» return/go back «老» «闆» «娘家» [now/changed]
  Alt (32%): we «要» return/go back «老» «闆» «娘家» (too much)

### 2/23
**[2/23 12:25 PM] 沒關係，那都已經是過去式了、現在最重要的就是把身體養好、賺了再多錢也沒有什麼比身體重要** (H=1.67)
  Primary: [you, 56%] no/not «關» «係» «，» «那» «都» «已經» is/am/are «過去» «式» [completed] «、» now «最» important «就是» «把» body/health «養好» «、» «賺» [completed] «再» «多» money «也» don't have «什麼» «比» body/health important
  Alt (22%): [I, 22%] no/not «關» «係» «，» «那» «都» «已經» is/am/are «過去» «式» [completed] «、» now «最» important «就是» «把» body/health «養好» «、» «賺» [completed] «再» «多» money «也» don't have «什麼» «比» body/health important
  Alt (17%): [we, 17%] no/not «關» «係» «，» «那» «都» «已經» is/am/are «過去» «式» [completed] «、» now «最» important «就是» «把» body/health «養好» «、» «賺» [completed] «再» «多» money «也» don't have «什麼» «比» body/health important

**[2/23 1:34 PM] 請問你目前身體有什麼狀況、有哪裡不舒服？要改進的？** (H=1.67)
  Primary: [you, 56%] «請» «問» you «目前» body/health have «什麼» «狀況» «、» have «哪裡» not «舒服» «？» «要» «改進» «？»
  Alt (22%): [I, 22%] «請» «問» you «目前» body/health have «什麼» «狀況» «、» have «哪裡» not «舒服» «？» «要» «改進» «？»
  Alt (17%): [we, 17%] «請» «問» you «目前» body/health have «什麼» «狀況» «、» have «哪裡» not «舒服» «？» «要» «改進» «？»

**[2/23 1:34 PM] 表姐的同學，他們家的小狗也都有帶量子環產品都變得很健康很活潑** (H=1.58)
  Primary: «表姐» «同學» «，» they «家» «小狗» «也» «都» have bring «量子» «環產品» «都» «變» «很» healthy «很» «活潑»
  Alt (33%): «表姐» «同學» «，» they «家» «小狗» «也» «都» have wear «量子» «環產品» «都» «變» «很» healthy «很» «活潑»
  Alt (33%): «表姐» «同學» «，» they «家» «小狗» «也» «都» have lead/guide «量子» «環產品» «都» «變» «很» healthy «很» «活潑»

**[2/23 1:34 PM] 這個影片是那些老師、他們都做了兩年、每個人每個月薪水都是幾百萬的薪水** (H=1.58)
  Primary: «這個» «影片» is/am/are «那些» «老師» «、» they «都» do/make [completed] «兩年» «、» «每個» «人» «每個» «月» salary «都» is/am/are «幾百萬» salary
  Alt (33%): «這個» «影片» is/am/are «那些» «老師» «、» they «都» work_as [completed] «兩年» «、» «每個» «人» «每個» «月» salary «都» is/am/are «幾百萬» salary
  Alt (33%): «這個» «影片» is/am/are «那些» «老師» «、» they «都» conduct [completed] «兩年» «、» «每個» «人» «每個» «月» salary «都» is/am/are «幾百萬» salary

**[2/23 2:14 PM] 這個就是你們美國人發明的沃倫博士、他自己帶的也很健康，也變年輕** (H=1.58)
  Primary: «這個» «就是» you all «美國» «人» «發明» «沃倫» «博士» «、» he oneself bring «也» «很» healthy «，» «也» «變» «年» «輕»
  Alt (33%): «這個» «就是» you all «美國» «人» «發明» «沃倫» «博士» «、» he oneself wear «也» «很» healthy «，» «也» «變» «年» «輕»
  Alt (33%): «這個» «就是» you all «美國» «人» «發明» «沃倫» «博士» «、» he oneself lead/guide «也» «很» healthy «，» «也» «變» «年» «輕»

**[2/23 2:14 PM] 這個是大家翻譯出來的功效跟好處** (H=1.00)
  Primary: «這個» is/am/are everyone «翻譯» «出來» «功效» «跟» good «處»
  Alt (50%): «這個» is/am/are everyone «翻譯» «出來» «功效» «跟» ok/agreed «處»

**[2/23 2:14 PM] 這個就是人家自己做的戴在脖子改善頸椎、改善全身、改善富貴包、它可以幫助頸椎打通全身** (H=1.58)
  Primary: «這個» «就是» «人家» oneself do/make wear «在» «脖子» improve «頸椎» «、» improve «全身» «、» improve «富貴» «包» «、» «它» «可以» «幫助» «頸椎» «打通» «全身»
  Alt (33%): «這個» «就是» «人家» oneself work_as wear «在» «脖子» improve «頸椎» «、» improve «全身» «、» improve «富貴» «包» «、» «它» «可以» «幫助» «頸椎» «打通» «全身»
  Alt (33%): «這個» «就是» «人家» oneself conduct wear «在» «脖子» improve «頸椎» «、» improve «全身» «、» improve «富貴» «包» «、» «它» «可以» «幫助» «頸椎» «打通» «全身»

**[2/23 2:14 PM] 等我的產品到了、我在打給你體驗看看有什麼改善** (H=1.00)
  Primary: I product arrive [completed] «、» I «在» «打給» you «體驗» «看看» «有什麼» improve
  Alt (50%): I product succeed [completed] «、» I «在» «打給» you «體驗» «看看» «有什麼» improve

**[2/23 3:48 PM] 你們都好棒** (H=1.00)
  Primary: you all «都» good great
  Alt (50%): you all «都» ok/agreed great

### 2/25
**[2/25 10:57 AM] 我跟我同事我們兩個在吃早餐了** (H=1.58)
  Primary: I «跟» I coworker we «兩個» «在» eat breakfast [completed]
  Alt (32%): I «跟» I coworker we «兩個» «在» eat breakfast [now/changed]
  Alt (32%): I «跟» I coworker we «兩個» «在» eat breakfast (too much)

**[2/25 10:57 AM] 針灸也很好，但是他不能治本** (H=1.00)
  Primary: «針灸» «也» «很» good «，» «但是» he «不能» «治本»
  Alt (50%): «針灸» «也» «很» ok/agreed «，» «但是» he «不能» «治本»

**[2/25 8:00 PM] 一定是的、** (H=1.85)
  Primary: [you, 37%] «一定» is/am/are «、»
  Alt (36%): [I, 36%] «一定» is/am/are «、»
  Alt (21%): [we, 21%] «一定» is/am/are «、»

### 2/26
**[2/26 8:02 AM] 祝你有美好的一天** (H=1.85)
  Primary: [I, 36%] «祝» you have «美好» «一天»
  Alt (36%): [you, 36%] «祝» you have «美好» «一天»
  Alt (22%): [we, 22%] «祝» you have «美好» «一天»

**[2/26 11:09 AM] 我從小到大，每天都有吃早餐** (H=1.00)
  Primary: I «從» «小» arrive «大» «，» «每天» «都» have eat breakfast
  Alt (50%): I «從» «小» succeed «大» «，» «每天» «都» have eat breakfast

**[2/26 3:38 PM] 欣廸** (H=1.72)
  Primary: [I, 50%] «欣» «廸»
  Alt (28%): [we, 28%] «欣» «廸»
  Alt (16%): [you, 16%] «欣» «廸»

**[2/26 4:19 PM] 林渼惠** (H=1.85)
  Primary: [I, 36%] «林» «渼» «惠»
  Alt (36%): [you, 36%] «林» «渼» «惠»
  Alt (22%): [we, 22%] «林» «渼» «惠»

**[2/26 6:01 PM] 是纽约的表姐幫忙取的** (H=1.85)
  Primary: [I, 36%] is/am/are «纽约» «表姐» help «忙取»
  Alt (36%): [you, 36%] is/am/are «纽约» «表姐» help «忙取»
  Alt (22%): [we, 22%] is/am/are «纽约» «表姐» help «忙取»

**[2/26 6:01 PM] 我們剛忙，好一對夫妻、現在準備吃午餐跟晚餐了** (H=2.00)
  Primary: we «剛忙» «，» good «一對» «夫妻» «、» now «準備» eat lunch «跟» dinner [completed]
  Alt (26%): we «剛忙» «，» ok/agreed «一對» «夫妻» «、» now «準備» eat lunch «跟» dinner [completed]
  Alt (24%): we «剛忙» «，» good «一對» «夫妻» «、» now «準備» eat lunch «跟» dinner [now/changed]

**[2/26 6:01 PM] 我們從小到大都這樣用、** (H=1.00)
  Primary: we «從» «小» arrive «大都» «這樣» «用» «、»
  Alt (50%): we «從» «小» succeed «大都» «這樣» «用» «、»

**[2/26 6:01 PM] 加油** (H=1.85)
  Primary: [you, 37%] keep it up/go for it
  Alt (36%): [I, 36%] keep it up/go for it
  Alt (21%): [we, 21%] keep it up/go for it

**[2/26 9:38 PM] 沒關係，我們的家人不會嘲笑大家的、因為他們都很善良** (H=1.85)
  Primary: [you, 37%] no/not «關» «係» «，» we family not «會» «嘲笑» everyone «、» «因為» they «都» «很» kind/good-hearted
  Alt (36%): [I, 36%] no/not «關» «係» «，» we family not «會» «嘲笑» everyone «、» «因為» they «都» «很» kind/good-hearted
  Alt (21%): [we, 21%] no/not «關» «係» «，» we family not «會» «嘲笑» everyone «、» «因為» they «都» «很» kind/good-hearted

### 2/27
**[2/27 4:19 PM] 加油** (H=1.85)
  Primary: [you, 37%] keep it up/go for it
  Alt (36%): [I, 36%] keep it up/go for it
  Alt (21%): [we, 21%] keep it up/go for it

**[2/27 4:19 PM] 你要走去哪裏** (H=1.58)
  Primary: you «要» walk go «哪»
  Alt (33%): you «要» leave go «哪»
  Alt (33%): you «要» go_through go «哪»

**[2/27 4:19 PM] 你是說你要去找工作** (H=1.58)
  Primary: you is/am/are say/speak you «要» go «找» work
  Alt (33%): you is/am/are scold you «要» go «找» work
  Alt (33%): you is/am/are mean you «要» go «找» work

**[2/27 4:54 PM] 好吃** (H=1.85)
  Primary: [you, 37%] «好吃»
  Alt (36%): [I, 36%] «好吃»
  Alt (21%): [we, 21%] «好吃»

**[2/27 5:45 PM] 很好** (H=1.00)
  Primary: «很» good
  Alt (50%): «很» ok/agreed

### 2/28
**[2/28 7:59 AM] 沒關係** (H=1.72)
  Primary: [I, 50%] no/not «關» «係»
  Alt (28%): [we, 28%] no/not «關» «係»
  Alt (16%): [you, 16%] no/not «關» «係»

**[2/28 7:59 AM] 最近預約的客人比較多，所以我們都比較忙一點** (H=1.85)
  Primary: [I, 36%] «最近» «預約» «客人» «比較» «多» «，» «所以» we «都» «比較» busy «一點»
  Alt (36%): [you, 36%] «最近» «預約» «客人» «比較» «多» «，» «所以» we «都» «比較» busy «一點»
  Alt (22%): [we, 22%] «最近» «預約» «客人» «比較» «多» «，» «所以» we «都» «比較» busy «一點»

**[2/28 10:04 AM] 我從小到大，每天都有吃早餐** (H=1.00)
  Primary: I «從» «小» arrive «大» «，» «每天» «都» have eat breakfast
  Alt (50%): I «從» «小» succeed «大» «，» «每天» «都» have eat breakfast

**[2/28 12:42 PM] 你們做的水煮蛋裡跟我一樣的做法嗎？** (H=2.00)
  Primary: you all do/make boiled egg «裡» «跟» I «做法» «？»
  Alt (25%): you all work_as boiled egg «裡» «跟» I «做法» «？»
  Alt (25%): you all conduct boiled egg «裡» «跟» I «做法» «？»

**[2/28 4:43 PM] 是的，她們都很會煮菜** (H=1.85)
  Primary: [you, 37%] is/am/are «，» they «都» «很» «會» «煮菜»
  Alt (36%): [I, 36%] is/am/are «，» they «都» «很» «會» «煮菜»
  Alt (21%): [we, 21%] is/am/are «，» they «都» «很» «會» «煮菜»

### 3/1
**[3/1 12:08 PM] 所以當然是當會計** (H=1.72)
  Primary: [I, 50%] «所以» «當然» is/am/are «當» «會計»
  Alt (28%): [we, 28%] «所以» «當然» is/am/are «當» «會計»
  Alt (16%): [you, 16%] «所以» «當然» is/am/are «當» «會計»

**[3/1 2:31 PM] 我從小到大都有吃早餐** (H=1.00)
  Primary: I «從» «小» arrive «大都» have eat breakfast
  Alt (50%): I «從» «小» succeed «大都» have eat breakfast

**[3/1 2:41 PM] 這樣很好、加油** (H=1.00)
  Primary: «這樣» «很» good «、» keep it up/go for it
  Alt (50%): «這樣» «很» ok/agreed «、» keep it up/go for it

**[3/1 2:41 PM] 是的** (H=1.72)
  Primary: [I, 50%] is/am/are
  Alt (28%): [we, 28%] is/am/are
  Alt (16%): [you, 16%] is/am/are

**[3/1 3:44 PM] 好** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/1 5:54 PM] 不用找中文版，我可以翻譯的、謝謝你** (H=1.85)
  Primary: [you, 37%] «不用» «找» «中文版» «，» I «可以» «翻譯» «、» thank you you
  Alt (36%): [I, 36%] «不用» «找» «中文版» «，» I «可以» «翻譯» «、» thank you you
  Alt (21%): [we, 21%] «不用» «找» «中文版» «，» I «可以» «翻譯» «、» thank you you

**[3/1 6:56 PM] 好** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

### 3/2
**[3/2 10:27 AM] 好的，謝謝你** (H=1.00)
  Primary: good «，» thank you you
  Alt (50%): ok/agreed «，» thank you you

**[3/2 11:33 AM] 她說你們這裡的Costco也有賣** (H=1.58)
  Primary: she say/speak you all «這裡» «Costco» «也» have sell
  Alt (33%): she scold you all «這裡» «Costco» «也» have sell
  Alt (33%): she mean you all «這裡» «Costco» «也» have sell

**[3/2 11:33 AM] 好** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/2 4:53 PM] 好吃** (H=1.72)
  Primary: [I, 50%] «好吃»
  Alt (28%): [we, 28%] «好吃»
  Alt (16%): [you, 16%] «好吃»

**[3/2 7:36 PM] 好的，謝謝你** (H=1.00)
  Primary: good «，» thank you you
  Alt (50%): ok/agreed «，» thank you you

**[3/2 7:57 PM] 好** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/2 7:57 PM] 好** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

### 3/3
**[3/3 6:57 PM] 老闆娘跟我同事兩個在用晚餐、等等我們要吃晚餐了** (H=1.58)
  Primary: «老» «闆» «娘» «跟» I coworker «兩個» «在» «用» dinner «、» we «要» eat dinner [completed]
  Alt (32%): «老» «闆» «娘» «跟» I coworker «兩個» «在» «用» dinner «、» we «要» eat dinner [now/changed]
  Alt (32%): «老» «闆» «娘» «跟» I coworker «兩個» «在» «用» dinner «、» we «要» eat dinner (too much)

**[3/3 8:51 PM] 加油** (H=1.85)
  Primary: [you, 37%] keep it up/go for it
  Alt (36%): [I, 36%] keep it up/go for it
  Alt (21%): [we, 21%] keep it up/go for it

### 3/4
**[3/4 9:18 AM] 祝你有愉快的一天** (H=1.85)
  Primary: [I, 36%] «祝» you have «愉快» «一天»
  Alt (36%): [you, 36%] «祝» you have «愉快» «一天»
  Alt (22%): [we, 22%] «祝» you have «愉快» «一天»

**[3/4 6:13 PM] 他們約時間、可以把身體治療好是好事** (H=1.00)
  Primary: they «約» time «、» «可以» «把» body/health «治療» good is/am/are «好事»
  Alt (50%): they «約» time «、» «可以» «把» body/health «治療» ok/agreed is/am/are «好事»

**[3/4 8:27 PM] 我們快下班了，我們老闆娘來接我們了** (H=1.58)
  Primary: we «快下班» [completed] «，» we «老» «闆» «娘» come «接» I «們» [completed]
  Alt (32%): we «快下班» [now/changed] «，» we «老» «闆» «娘» come «接» I «們» [now/changed]
  Alt (32%): we «快下班» (too much) «，» we «老» «闆» «娘» come «接» I «們» (too much)

### 3/5
**[3/5 11:11 AM] 好的** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/5 11:11 AM] 也祝你有愉快的一天** (H=1.85)
  Primary: [I, 36%] «也» «祝» you have «愉快» «一天»
  Alt (36%): [you, 36%] «也» «祝» you have «愉快» «一天»
  Alt (22%): [we, 22%] «也» «祝» you have «愉快» «一天»

**[3/5 5:27 PM] 晚上好** (H=1.00)
  Primary: evening good
  Alt (50%): evening ok/agreed

**[3/5 5:31 PM] 好、我先去忙** (H=1.00)
  Primary: good «、» I «先» go busy
  Alt (50%): ok/agreed «、» I «先» go busy

**[3/5 9:04 PM] 好晚安** (H=1.00)
  Primary: good good night
  Alt (50%): ok/agreed good night

### 3/6
**[3/6 12:21 PM] 早餐吃了** (H=1.58)
  Primary: breakfast eat [completed]
  Alt (32%): breakfast eat [now/changed]
  Alt (32%): breakfast eat (too much)

**[3/6 12:21 PM] 好的** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/6 12:21 PM] 好的** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/6 2:30 PM] 活到老、學到老、是好事** (H=1.85)
  Primary: [you, 37%] «活到老» «、» «學到» «老» «、» is/am/are «好事»
  Alt (36%): [I, 36%] «活到老» «、» «學到» «老» «、» is/am/are «好事»
  Alt (21%): [we, 21%] «活到老» «、» «學到» «老» «、» is/am/are «好事»

**[3/6 2:49 PM] 現在的時機不適合去旅行、適合多學習、以後都用的到** (H=1.00)
  Primary: now «時機» not «適合» go «旅行» «、» «適合» «多» study/learn «、» «以» «後» «都» «用» arrive
  Alt (50%): now «時機» not «適合» go «旅行» «、» «適合» «多» study/learn «、» «以» «後» «都» «用» succeed

**[3/6 9:33 PM] 我們下班回來老闆娘他們家了** (H=1.58)
  Primary: we «下班» come back «老» «闆» «娘» he «們» «家» [completed]
  Alt (32%): we «下班» come back «老» «闆» «娘» he «們» «家» [now/changed]
  Alt (32%): we «下班» come back «老» «闆» «娘» he «們» «家» (too much)

### 3/7
**[3/7 8:49 AM] 是的，我現在這個只是暫時的在賺取開店的資金** (H=1.85)
  Primary: [you, 37%] is/am/are «，» I now «這個» «只是» «暫時» «在» «賺取» «開店» «資金»
  Alt (36%): [I, 36%] is/am/are «，» I now «這個» «只是» «暫時» «在» «賺取» «開店» «資金»
  Alt (21%): [we, 21%] is/am/are «，» I now «這個» «只是» «暫時» «在» «賺取» «開店» «資金»

**[3/7 8:49 AM] 好的，謝謝你** (H=1.00)
  Primary: good «，» thank you you
  Alt (50%): ok/agreed «，» thank you you

**[3/7 8:49 AM] 你也要認真復健，把身體顧好、現在的時機、平安健康最重要** (H=1.00)
  Primary: you «也» «要認» «真» «復» «健» «，» «把» body/health «顧» good «、» now «時機» «、» peace/safe healthy «最» important
  Alt (50%): you «也» «要認» «真» «復» «健» «，» «把» body/health «顧» ok/agreed «、» now «時機» «、» peace/safe healthy «最» important

### 3/8
**[3/8 11:50 AM] 加油、最好多喝溫開水、注意安全** (H=1.67)
  Primary: [you, 56%] keep it up/go for it «、» «最好» «多» drink «溫開水» «、» «注意安全»
  Alt (22%): [I, 22%] keep it up/go for it «、» «最好» «多» drink «溫開水» «、» «注意安全»
  Alt (17%): [we, 17%] keep it up/go for it «、» «最好» «多» drink «溫開水» «、» «注意安全»

**[3/8 11:50 AM] 你有說過42** (H=1.58)
  Primary: you have say/speak «42»
  Alt (33%): you have scold «42»
  Alt (33%): you have mean «42»

**[3/8 11:50 AM] 不會、人只要平安健康一年只有+1歲** (H=1.67)
  Primary: [you, 56%] not «會» «、» «人» «只要» peace/safe healthy «一年» «只有» «+» «1» «歲»
  Alt (22%): [I, 22%] not «會» «、» «人» «只要» peace/safe healthy «一年» «只有» «+» «1» «歲»
  Alt (17%): [we, 17%] not «會» «、» «人» «只要» peace/safe healthy «一年» «只有» «+» «1» «歲»

**[3/8 12:52 PM] 好** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/8 6:27 PM] 是的，超級超級的好吃** (H=1.85)
  Primary: [you, 37%] is/am/are «，» «超級» «超級» «好吃»
  Alt (36%): [I, 36%] is/am/are «，» «超級» «超級» «好吃»
  Alt (21%): [we, 21%] is/am/are «，» «超級» «超級» «好吃»

### 3/9
**[3/9 9:33 AM] 也祝你有愉快的一天** (H=1.85)
  Primary: [you, 37%] «也» «祝» you have «愉快» «一天»
  Alt (36%): [I, 36%] «也» «祝» you have «愉快» «一天»
  Alt (21%): [we, 21%] «也» «祝» you have «愉快» «一天»

**[3/9 10:27 AM] 加油** (H=1.85)
  Primary: [you, 37%] keep it up/go for it
  Alt (36%): [I, 36%] keep it up/go for it
  Alt (21%): [we, 21%] keep it up/go for it

**[3/9 9:19 PM] 好的晚安** (H=1.00)
  Primary: good good night
  Alt (50%): ok/agreed good night

### 3/10
**[3/10 6:36 PM] 不是慢慢吃、要吃流質的東西、就是軟的或者是粥** (H=1.67)
  Primary: [you, 56%] «不是» slowly/take your time eat «、» «要» eat «流質» «東西» «、» «就是» «軟» «或者» is/am/are «粥»
  Alt (22%): [I, 22%] «不是» slowly/take your time eat «、» «要» eat «流質» «東西» «、» «就是» «軟» «或者» is/am/are «粥»
  Alt (17%): [we, 17%] «不是» slowly/take your time eat «、» «要» eat «流質» «東西» «、» «就是» «軟» «或者» is/am/are «粥»

**[3/10 6:36 PM] 可以去外面買簡單的吃** (H=1.85)
  Primary: [you, 37%] «可以» go «外面» buy simple eat
  Alt (36%): [I, 36%] «可以» go «外面» buy simple eat
  Alt (21%): [we, 21%] «可以» go «外面» buy simple eat

**[3/10 9:10 PM] 好的，晚安** (H=1.00)
  Primary: good «，» good night
  Alt (50%): ok/agreed «，» good night

### 3/11
**[3/11 10:16 AM] 很好** (H=1.00)
  Primary: «很» good
  Alt (50%): «很» ok/agreed

**[3/11 6:49 PM] 吃這個很棒** (H=1.85)
  Primary: [you, 37%] eat «這個» «很棒»
  Alt (36%): [I, 36%] eat «這個» «很棒»
  Alt (21%): [we, 21%] eat «這個» «很棒»

**[3/11 7:31 PM] 辣椒對身體好** (H=1.00)
  Primary: «辣椒» right/correct body/health good
  Alt (50%): «辣椒» right/correct body/health ok/agreed

### 3/12
**[3/12 7:30 PM] 沒關係、只要喜歡吃都是好的** (H=1.95)
  Primary: [you, 56%] no/not «關» «係» «、» «只要» like eat «都» is/am/are good
  Alt (36%): [you, 56%] no/not «關» «係» «、» «只要» like eat «都» is/am/are ok/agreed
  Alt (14%): [I, 22%] no/not «關» «係» «、» «只要» like eat «都» is/am/are good

**[3/12 10:08 PM] 好的晚安** (H=1.00)
  Primary: good good night
  Alt (50%): ok/agreed good night

### 3/13
**[3/13 11:23 AM] 貴了一點、自己喝好一點沒關係** (H=1.00)
  Primary: expensive [completed] «一點» «、» oneself drink good «一點» no/not «關» «係»
  Alt (50%): expensive [completed] «一點» «、» oneself drink ok/agreed «一點» no/not «關» «係»

### 3/14
**[3/14 9:39 PM] 這個壽司可以吃對身體好、但是這個生魚片盡量不要吃、因為那都不是極速的裡面會很多細菌對身體不好** (H=1.00)
  Primary: «這個» «壽司» «可以» eat right/correct body/health good «、» «但是» «這個» «生» «魚片» «盡量» «不要» eat «、» «因為» «那» «都» «不是» «極速» «裡面» «會» «很多» «細菌» right/correct body/health «不好»
  Alt (50%): «這個» «壽司» «可以» eat right/correct body/health ok/agreed «、» «但是» «這個» «生» «魚片» «盡量» «不要» eat «、» «因為» «那» «都» «不是» «極速» «裡面» «會» «很多» «細菌» right/correct body/health «不好»

**[3/14 9:45 PM] 這是我在百度幫你查得給你做參考** (H=1.58)
  Primary: «這» is/am/are I «在» «百度» help you «查得» «給» you do/make «參考»
  Alt (33%): «這» is/am/are I «在» «百度» help you «查得» «給» you work_as «參考»
  Alt (33%): «這» is/am/are I «在» «百度» help you «查得» «給» you conduct «參考»

**[3/14 9:49 PM] 喜歡吃都沒關係、但是一定要吃熟的東西** (H=1.67)
  Primary: [you, 56%] like eat «都» no/not «關» «係» «、» «但是» «一定» «要» «吃熟» «東西»
  Alt (22%): [I, 22%] like eat «都» no/not «關» «係» «、» «但是» «一定» «要» «吃熟» «東西»
  Alt (17%): [we, 17%] like eat «都» no/not «關» «係» «、» «但是» «一定» «要» «吃熟» «東西»

### 3/15
**[3/15 10:06 AM] 才要來吃** (H=1.67)
  Primary: [you, 56%] «才» «要» come eat
  Alt (22%): [I, 22%] «才» «要» come eat
  Alt (17%): [we, 17%] «才» «要» come eat

**[3/15 10:22 AM] 沒事、** (H=1.85)
  Primary: [I, 36%] it's nothing/no problem «、»
  Alt (36%): [you, 36%] it's nothing/no problem «、»
  Alt (22%): [we, 22%] it's nothing/no problem «、»

**[3/15 1:47 PM] 學會我們台灣的話也很好、多種語言有好處** (H=1.58)
  Primary: «學會» we Taiwan «話» «也» «很» good «、» «多種» «語言» have good «處»
  Alt (33%): «學會» we Taiwan «話» «也» «很» good «、» «多種» «語言» have good «處»
  Alt (33%): «學會» we Taiwan «話» «也» «很» ok/agreed «、» «多種» «語言» have ok/agreed «處»

**[3/15 2:10 PM] 目前沒有** (H=1.85)
  Primary: [I, 36%] «目前» don't have
  Alt (36%): [you, 36%] «目前» don't have
  Alt (22%): [we, 22%] «目前» don't have

**[3/15 7:36 PM] 對好吃** (H=1.85)
  Primary: [I, 36%] right/correct «好吃»
  Alt (36%): [you, 36%] right/correct «好吃»
  Alt (22%): [we, 22%] right/correct «好吃»

**[3/15 10:39 PM] 明天再聊** (H=1.85)
  Primary: [I, 36%] tomorrow «再聊»
  Alt (36%): [you, 36%] tomorrow «再聊»
  Alt (22%): [we, 22%] tomorrow «再聊»

### 3/16
**[3/16 11:34 AM] 中午好** (H=1.00)
  Primary: noon good
  Alt (50%): noon ok/agreed

**[3/16 1:21 PM] 今天忙** (H=1.85)
  Primary: [I, 36%] today busy
  Alt (36%): [you, 36%] today busy
  Alt (22%): [we, 22%] today busy

**[3/16 2:16 PM] 好吃** (H=1.85)
  Primary: [I, 36%] «好吃»
  Alt (36%): [you, 36%] «好吃»
  Alt (22%): [we, 22%] «好吃»

### 3/17
**[3/17 12:40 PM] 好的，出去玩再寄漂亮照片分享，謝謝你** (H=1.00)
  Primary: good «，» «出去玩» «再寄» «漂亮» «照片» «分享» «，» thank you you
  Alt (50%): ok/agreed «，» «出去玩» «再寄» «漂亮» «照片» «分享» «，» thank you you

**[3/17 4:36 PM] 好** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/17 11:15 PM] 好的、謝謝你、晚安** (H=1.00)
  Primary: good «、» thank you you «、» good night
  Alt (50%): ok/agreed «、» thank you you «、» good night

### 3/18
**[3/18 10:07 AM] 好吃** (H=1.85)
  Primary: [I, 36%] «好吃»
  Alt (36%): [you, 36%] «好吃»
  Alt (22%): [we, 22%] «好吃»

**[3/18 10:41 AM] 很好** (H=1.00)
  Primary: «很» good
  Alt (50%): «很» ok/agreed

### 3/19
**[3/19 10:17 AM] 你吃早餐了沒** (H=1.58)
  Primary: you eat breakfast [completed] no/not
  Alt (32%): you eat breakfast [now/changed] no/not
  Alt (32%): you eat breakfast (too much) no/not

**[3/19 10:56 AM] 是龍抬頭的日子** (H=1.85)
  Primary: [I, 36%] is/am/are «龍» «抬頭» «日子»
  Alt (36%): [you, 36%] is/am/are «龍» «抬頭» «日子»
  Alt (22%): [we, 22%] is/am/are «龍» «抬頭» «日子»

**[3/19 10:56 AM] 可以找時間** (H=1.85)
  Primary: [I, 36%] «可以» «找» time
  Alt (36%): [you, 36%] «可以» «找» time
  Alt (22%): [we, 22%] «可以» «找» time

**[3/19 10:56 AM] 拿剪刀** (H=1.85)
  Primary: [I, 36%] «拿» «剪刀»
  Alt (36%): [you, 36%] «拿» «剪刀»
  Alt (22%): [we, 22%] «拿» «剪刀»

**[3/19 10:56 AM] 明天是一整年剪頭髮最好的日子、剪了一次一整年都好運連連** (H=1.95)
  Primary: [you, 56%] tomorrow is/am/are «一» «整年» «剪» «頭» «髮» «最好» «日子» «、» «剪» [completed] «一次» «一» «整年» «都» good «運» «連連»
  Alt (36%): [you, 56%] tomorrow is/am/are «一» «整年» «剪» «頭» «髮» «最好» «日子» «、» «剪» [completed] «一次» «一» «整年» «都» ok/agreed «運» «連連»
  Alt (14%): [I, 22%] tomorrow is/am/are «一» «整年» «剪» «頭» «髮» «最好» «日子» «、» «剪» [completed] «一次» «一» «整年» «都» good «運» «連連»

**[3/19 11:15 AM] 我是說不要來店裡浪費錢、時機很不好、按摩只是浪費錢沒什麼作用** (H=1.58)
  Primary: I is/am/are say/speak «不要» come «店» «裡» «浪費» money «、» «時機» «很» «不好» «、» «按摩» «只是» «浪費錢» no/not «什麼» «作用»
  Alt (33%): I is/am/are scold «不要» come «店» «裡» «浪費» money «、» «時機» «很» «不好» «、» «按摩» «只是» «浪費錢» no/not «什麼» «作用»
  Alt (33%): I is/am/are mean «不要» come «店» «裡» «浪費» money «、» «時機» «很» «不好» «、» «按摩» «只是» «浪費錢» no/not «什麼» «作用»

**[3/19 11:15 AM] 你是說你太多錢沒地方發是嗎？** (H=2.00)
  Primary: you is/am/are say/speak you «太» «多» money no/not «地方» «發是» «？»
  Alt (25%): you is/am/are scold you «太» «多» money no/not «地方» «發是» «？»
  Alt (25%): you is/am/are mean you «太» «多» money no/not «地方» «發是» «？»

**[3/19 11:15 AM] 按摩只是浪費時間又浪費錢、根本沒什麼作用、大家都知道的人家只是在打發時間來按摩、** (H=1.85)
  Primary: [I, 36%] «按摩» «只是» «浪費» time «又» «浪費» money «、» «根本» no/not «什麼» «作用» «、» everyone «都» know «人家» «只是» «在» «打發» time come «按摩» «、»
  Alt (36%): [you, 36%] «按摩» «只是» «浪費» time «又» «浪費» money «、» «根本» no/not «什麼» «作用» «、» everyone «都» know «人家» «只是» «在» «打發» time come «按摩» «、»
  Alt (22%): [we, 22%] «按摩» «只是» «浪費» time «又» «浪費» money «、» «根本» no/not «什麼» «作用» «、» everyone «都» know «人家» «只是» «在» «打發» time come «按摩» «、»

**[3/19 11:15 AM] 請問你現在存了多少錢？** (H=1.85)
  Primary: [I, 36%] «請» «問» you now save [completed] «多少» money «？»
  Alt (36%): [you, 36%] «請» «問» you now save [completed] «多少» money «？»
  Alt (22%): [we, 22%] «請» «問» you now save [completed] «多少» money «？»

**[3/19 11:27 AM] 一個月收入3800扣掉支出1900、那也一個月剩下1900** (H=1.85)
  Primary: [I, 36%] «一個» «月» «收入» «3800» «扣掉» «支出» «1900» «、» «那» «也» «一個» «月» «剩下» «1900»
  Alt (36%): [you, 36%] «一個» «月» «收入» «3800» «扣掉» «支出» «1900» «、» «那» «也» «一個» «月» «剩下» «1900»
  Alt (22%): [we, 22%] «一個» «月» «收入» «3800» «扣掉» «支出» «1900» «、» «那» «也» «一個» «月» «剩下» «1900»

**[3/19 11:27 AM] 所以不要亂亂花錢、現在全世界這麼亂，只有平平安安健健康康最重要** (H=1.67)
  Primary: [you, 56%] «所以» «不要» «亂» «亂» «花» money «、» now «全世界» «這麼» «亂» «，» «只有» «平平安安» «健健康康» «最» important
  Alt (22%): [I, 22%] «所以» «不要» «亂» «亂» «花» money «、» now «全世界» «這麼» «亂» «，» «只有» «平平安安» «健健康康» «最» important
  Alt (17%): [we, 17%] «所以» «不要» «亂» «亂» «花» money «、» now «全世界» «這麼» «亂» «，» «只有» «平平安安» «健健康康» «最» important

**[3/19 11:52 AM] 加油** (H=1.85)
  Primary: [I, 36%] keep it up/go for it
  Alt (36%): [you, 36%] keep it up/go for it
  Alt (22%): [we, 22%] keep it up/go for it

**[3/19 12:00 PM] 哈哈、是的** (H=1.85)
  Primary: [I, 36%] «哈哈» «、» is/am/are
  Alt (36%): [you, 36%] «哈哈» «、» is/am/are
  Alt (22%): [we, 22%] «哈哈» «、» is/am/are

**[3/19 12:21 PM] 那很好** (H=1.00)
  Primary: «那» «很» good
  Alt (50%): «那» «很» ok/agreed

**[3/19 12:21 PM] 所以你是說、你們全家人只有你而已** (H=1.58)
  Primary: «所以» you is/am/are say/speak «、» you all «全家人» «只有» you
  Alt (33%): «所以» you is/am/are scold «、» you all «全家人» «只有» you
  Alt (33%): «所以» you is/am/are mean «、» you all «全家人» «只有» you

**[3/19 12:21 PM] 你挑選女朋友的條件開出來給我、我幫你認真找看看、從我的好朋友裡面找一個** (H=1.00)
  Primary: you «挑選» «女朋友» «條件» «開出» come «給» I «、» I help you «認真» «找» «看看» «、» «從» I good friend «裡面» «找» «一個»
  Alt (50%): you «挑選» «女朋友» «條件» «開出» come «給» I «、» I help you «認真» «找» «看看» «、» «從» I ok/agreed friend «裡面» «找» «一個»

**[3/19 12:21 PM] 我認真幫你找這三個生肖的女孩、到時候我問好他們發照片跟你挑一個** (H=1.58)
  Primary: I «認真» help you «找» «這» «三個» «生肖» «女孩» «、» arrive «時候» I «問» good they «發» «照片» «跟» you «挑» «一個»
  Alt (33%): I «認真» help you «找» «這» «三個» «生肖» «女孩» «、» succeed «時候» I «問» good they «發» «照片» «跟» you «挑» «一個»
  Alt (33%): I «認真» help you «找» «這» «三個» «生肖» «女孩» «、» arrive «時候» I «問» ok/agreed they «發» «照片» «跟» you «挑» «一個»

**[3/19 1:05 PM] 我先去忙、昨天預約的一對夫妻來了** (H=1.58)
  Primary: I «先» go busy «、» yesterday «預約» «一對» «夫妻» come [completed]
  Alt (32%): I «先» go busy «、» yesterday «預約» «一對» «夫妻» come [now/changed]
  Alt (32%): I «先» go busy «、» yesterday «預約» «一對» «夫妻» come (too much)

**[3/19 2:11 PM] 好的、你的針灸治療** (H=1.00)
  Primary: good «、» you «針灸» «治療»
  Alt (50%): ok/agreed «、» you «針灸» «治療»

**[3/19 4:16 PM] 好** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/19 6:28 PM] 剛剛要來吃** (H=1.67)
  Primary: [you, 56%] «剛剛» «要» come eat
  Alt (22%): [I, 22%] «剛剛» «要» come eat
  Alt (17%): [we, 17%] «剛剛» «要» come eat

**[3/19 6:28 PM] 是的，我同事很會做菜** (H=1.85)
  Primary: [I, 36%] is/am/are «，» I coworker «很» «會» «做菜»
  Alt (36%): [you, 36%] is/am/are «，» I coworker «很» «會» «做菜»
  Alt (22%): [we, 22%] is/am/are «，» I coworker «很» «會» «做菜»

### 3/20
**[3/20 9:40 AM] 那個是吐司裡面加了起司** (H=1.58)
  Primary: «那個» is/am/are «吐司» «裡面» «加» [completed] «起司»
  Alt (32%): «那個» is/am/are «吐司» «裡面» «加» [now/changed] «起司»
  Alt (32%): «那個» is/am/are «吐司» «裡面» «加» (too much) «起司»

**[3/20 11:31 AM] 我沒有那麼快回去、還要在紐約把量子環產品的店做好、到時候可以美國跟台灣二邊住幾個月** (H=1.00)
  Primary: I don't have «那麼» «快回去» «、» «還要» «在» New York «把» «量子» «環產品» «店» «做好» «、» arrive «時候» «可以» «美國» «跟» Taiwan «二» «邊» live «幾個» «月»
  Alt (50%): I don't have «那麼» «快回去» «、» «還要» «在» New York «把» «量子» «環產品» «店» «做好» «、» succeed «時候» «可以» «美國» «跟» Taiwan «二» «邊» live «幾個» «月»

**[3/20 11:31 AM] 你可以去紐約找我們、我帶你跟我所有朋友一起吃飯** (H=1.58)
  Primary: you «可以» go New York «找» we «、» I bring you «跟» I «所有» friend «一起» eat rice/meal
  Alt (33%): you «可以» go New York «找» we «、» I wear you «跟» I «所有» friend «一起» eat rice/meal
  Alt (33%): you «可以» go New York «找» we «、» I lead/guide you «跟» I «所有» friend «一起» eat rice/meal

**[3/20 12:19 PM] 我從小到大都不曾對別人、發號施令** (H=1.00)
  Primary: I «從» «小» arrive «大都» «不曾» right/correct «別人» «、» «發號» «施令»
  Alt (50%): I «從» «小» succeed «大都» «不曾» right/correct «別人» «、» «發號» «施令»

**[3/20 12:19 PM] 哈哈、沒事了、每個人都有過去、好的留著、壞的忘記、不要一直想不開心的事情、對身體健康無益** (H=1.95)
  Primary: [you, 56%] «哈哈» «、» it's nothing/no problem [completed] «、» «每個» «人» «都» have «過去» «、» good «留著» «、» «壞» «忘記» «、» «不要» «一直» want/think not happy «事情» «、» right/correct body/health healthy «無益»
  Alt (36%): [you, 56%] «哈哈» «、» it's nothing/no problem [completed] «、» «每個» «人» «都» have «過去» «、» ok/agreed «留著» «、» «壞» «忘記» «、» «不要» «一直» want/think not happy «事情» «、» right/correct body/health healthy «無益»
  Alt (14%): [I, 22%] «哈哈» «、» it's nothing/no problem [completed] «、» «每個» «人» «都» have «過去» «、» good «留著» «、» «壞» «忘記» «、» «不要» «一直» want/think not happy «事情» «、» right/correct body/health healthy «無益»

**[3/20 1:09 PM] 加油** (H=1.85)
  Primary: [I, 36%] keep it up/go for it
  Alt (36%): [you, 36%] keep it up/go for it
  Alt (22%): [we, 22%] keep it up/go for it

**[3/20 2:43 PM] 薯條雞塊洋蔥是買的、其他是我朋友做的** (H=1.58)
  Primary: «薯條» «雞塊» «洋蔥» is/am/are buy «、» «其他» is/am/are I friend do/make
  Alt (33%): «薯條» «雞塊» «洋蔥» is/am/are buy «、» «其他» is/am/are I friend work_as
  Alt (33%): «薯條» «雞塊» «洋蔥» is/am/are buy «、» «其他» is/am/are I friend conduct

**[3/20 4:57 PM] 壞運去、好运来** (H=1.85)
  Primary: [I, 36%] «壞» «運去» «、» «好运来»
  Alt (36%): [you, 36%] «壞» «運去» «、» «好运来»
  Alt (22%): [we, 22%] «壞» «運去» «、» «好运来»

**[3/20 4:57 PM] 我去忙了，你快去吃晚餐吧** (H=2.00)
  Primary: I go busy [completed] «，» you «快» go eat dinner (let's / how about)
  Alt (25%): I go busy [completed] «，» you «快» go eat dinner (fine / I suppose)
  Alt (25%): I go busy [completed] «，» you «快» go eat dinner (I think / probably)

**[3/20 8:37 PM] 麵條要跟豆腐分開煮** (H=1.67)
  Primary: [you, 56%] «麵» «條» «要» «跟» «豆腐» «分開» cook
  Alt (22%): [I, 22%] «麵» «條» «要» «跟» «豆腐» «分開» cook
  Alt (17%): [we, 17%] «麵» «條» «要» «跟» «豆腐» «分開» cook

**[3/20 8:37 PM] 大家不是都說你們這外州比較便宜** (H=1.58)
  Primary: everyone «不是» «都» say/speak you all «這» «外州» «比較» «便宜»
  Alt (33%): everyone «不是» «都» scold you all «這» «外州» «比較» «便宜»
  Alt (33%): everyone «不是» «都» mean you all «這» «外州» «比較» «便宜»

**[3/20 8:37 PM] 這個是台湾第六個妹妹、她的公公婆婆寄過來給我的、我已經用了三年** (H=1.58)
  Primary: «這個» is/am/are «台湾» «第六» «個» younger sister «、» she «公公» «婆婆» «寄» «過來» «給» I «、» I «已經» «用» [completed] «三年»
  Alt (32%): «這個» is/am/are «台湾» «第六» «個» younger sister «、» she «公公» «婆婆» «寄» «過來» «給» I «、» I «已經» «用» [now/changed] «三年»
  Alt (32%): «這個» is/am/are «台湾» «第六» «個» younger sister «、» she «公公» «婆婆» «寄» «過來» «給» I «、» I «已經» «用» (too much) «三年»

**[3/20 8:37 PM] 我們這種好的茶壺就是泡好的台灣高山茶** (H=1.58)
  Primary: we «這種» good «茶壺» «就是» «泡» good Taiwan «高山» «茶»
  Alt (33%): we «這種» good «茶壺» «就是» «泡» good Taiwan «高山» «茶»
  Alt (33%): we «這種» ok/agreed «茶壺» «就是» «泡» ok/agreed Taiwan «高山» «茶»

**[3/20 8:37 PM] 但是他們大家都說太浪費錢了，所以讓我去跟他們大家住** (H=1.58)
  Primary: «但是» they everyone «都» say/speak «太浪» «費錢» [completed] «，» «所以» «讓» I go «跟» they everyone live
  Alt (33%): «但是» they everyone «都» scold «太浪» «費錢» [completed] «，» «所以» «讓» I go «跟» they everyone live
  Alt (33%): «但是» they everyone «都» mean «太浪» «費錢» [completed] «，» «所以» «讓» I go «跟» they everyone live

**[3/20 8:37 PM] 你們美國消費實在太貴了** (H=1.58)
  Primary: you all «美國» «消費» «實在» «太» expensive [completed]
  Alt (32%): you all «美國» «消費» «實在» «太» expensive [now/changed]
  Alt (32%): you all «美國» «消費» «實在» «太» expensive (too much)

**[3/20 8:37 PM] 沒事、等改天去紐約跟我們大家吃飯、你再看看喜歡那裡的環境以後可以搬來纽约方便** (H=1.85)
  Primary: [I, 36%] it's nothing/no problem «、» «改天» go New York «跟» we everyone eat rice/meal «、» you «再» «看看» like «那裡» «環境» «以» «後» «可以» «搬來» «纽约» «方便»
  Alt (36%): [you, 36%] it's nothing/no problem «、» «改天» go New York «跟» we everyone eat rice/meal «、» you «再» «看看» like «那裡» «環境» «以» «後» «可以» «搬來» «纽约» «方便»
  Alt (22%): [we, 22%] it's nothing/no problem «、» «改天» go New York «跟» we everyone eat rice/meal «、» you «再» «看看» like «那裡» «環境» «以» «後» «可以» «搬來» «纽约» «方便»

**[3/20 8:37 PM] 是** (H=1.85)
  Primary: [I, 36%] is/am/are
  Alt (36%): [you, 36%] is/am/are
  Alt (22%): [we, 22%] is/am/are

**[3/20 8:37 PM] 最好不要熬夜，對身體不好** (H=1.67)
  Primary: [you, 56%] «最好» «不要» «熬夜» «，» right/correct body/health «不好»
  Alt (22%): [I, 22%] «最好» «不要» «熬夜» «，» right/correct body/health «不好»
  Alt (17%): [we, 17%] «最好» «不要» «熬夜» «，» right/correct body/health «不好»

**[3/20 9:50 PM] 加油** (H=1.85)
  Primary: [I, 36%] keep it up/go for it
  Alt (36%): [you, 36%] keep it up/go for it
  Alt (22%): [we, 22%] keep it up/go for it

### 3/21
**[3/21 9:27 AM] 好的、謝謝你** (H=1.00)
  Primary: good «、» thank you you
  Alt (50%): ok/agreed «、» thank you you

**[3/21 9:27 AM] 祝你有愉快的一天** (H=1.85)
  Primary: [I, 36%] «祝» you have «愉快» «一天»
  Alt (36%): [you, 36%] «祝» you have «愉快» «一天»
  Alt (22%): [we, 22%] «祝» you have «愉快» «一天»

**[3/21 9:27 AM] 吃早餐** (H=1.85)
  Primary: [I, 36%] eat breakfast
  Alt (36%): [you, 36%] eat breakfast
  Alt (22%): [we, 22%] eat breakfast

**[3/21 11:59 AM] 好的，小心慢慢開車注意安全** (H=1.00)
  Primary: good «，» be careful slowly/take your time drive «注意安全»
  Alt (50%): ok/agreed «，» be careful slowly/take your time drive «注意安全»

**[3/21 1:40 PM] 好的** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/21 7:32 PM] 你吃了** (H=1.58)
  Primary: you eat [completed]
  Alt (32%): you eat [now/changed]
  Alt (32%): you eat (too much)

**[3/21 7:32 PM] 冥想很好** (H=1.00)
  Primary: «冥想» «很» good
  Alt (50%): «冥想» «很» ok/agreed

**[3/21 7:32 PM] 好的** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/21 8:23 PM] 很好** (H=1.00)
  Primary: «很» good
  Alt (50%): «很» ok/agreed

**[3/21 8:23 PM] 它是一種對胃很好的魚** (H=1.00)
  Primary: «它» is/am/are «一種» right/correct «胃» «很» good «魚»
  Alt (50%): «它» is/am/are «一種» right/correct «胃» «很» ok/agreed «魚»

**[3/21 9:09 PM] 吃自己喜歡吃的、人只要平安健康什麼都好、** (H=1.95)
  Primary: [you, 56%] eat oneself like eat «、» «人» «只要» peace/safe healthy «什麼» «都» good «、»
  Alt (36%): [you, 56%] eat oneself like eat «、» «人» «只要» peace/safe healthy «什麼» «都» ok/agreed «、»
  Alt (14%): [I, 22%] eat oneself like eat «、» «人» «只要» peace/safe healthy «什麼» «都» good «、»

**[3/21 9:09 PM] 喝可樂對身體不好、最好是喝溫開水比冰開水好** (H=1.95)
  Primary: [you, 56%] drink «可» «樂» right/correct body/health «不好» «、» «最好» is/am/are drink «溫開水» «比» «冰» «開水» good
  Alt (36%): [you, 56%] drink «可» «樂» right/correct body/health «不好» «、» «最好» is/am/are drink «溫開水» «比» «冰» «開水» ok/agreed
  Alt (14%): [I, 22%] drink «可» «樂» right/correct body/health «不好» «、» «最好» is/am/are drink «溫開水» «比» «冰» «開水» good

**[3/21 9:09 PM] 我們要回去老闆娘的家了、** (H=1.58)
  Primary: we «要» go back «老» «闆» «娘» «家» [completed] «、»
  Alt (32%): we «要» go back «老» «闆» «娘» «家» [now/changed] «、»
  Alt (32%): we «要» go back «老» «闆» «娘» «家» (too much) «、»

### 3/22
**[3/22 4:35 PM] 好的** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

**[3/22 7:11 PM] 等一下吃** (H=1.85)
  Primary: [I, 36%] «一下» eat
  Alt (36%): [you, 36%] «一下» eat
  Alt (22%): [we, 22%] «一下» eat

**[3/22 9:02 PM] 去年我們家的荔枝、爸爸他去馬路上賣、老七比帶她女兒去幫忙賣** (H=1.58)
  Primary: «去年» we «家» «荔枝» «、» dad he go «馬» «路上» sell «、» «老七» «比» bring she «女兒» go help busy sell
  Alt (33%): «去年» we «家» «荔枝» «、» dad he go «馬» «路上» sell «、» «老七» «比» wear she «女兒» go help busy sell
  Alt (33%): «去年» we «家» «荔枝» «、» dad he go «馬» «路上» sell «、» «老七» «比» lead/guide she «女兒» go help busy sell

**[3/22 10:24 PM] 好** (H=1.00)
  Primary: good
  Alt (50%): ok/agreed

### 3/23
**[3/23 10:41 AM] 沒關係，你講英文、大家都會翻譯** (H=1.85)
  Primary: [I, 36%] no/not «關» «係» «，» you «講» «英文» «、» everyone «都» «會» «翻譯»
  Alt (36%): [you, 36%] no/not «關» «係» «，» you «講» «英文» «、» everyone «都» «會» «翻譯»
  Alt (22%): [we, 22%] no/not «關» «係» «，» you «講» «英文» «、» everyone «都» «會» «翻譯»

**[3/23 10:41 AM] 我們剛剛吃好早餐** (H=1.00)
  Primary: we «剛剛» eat good breakfast
  Alt (50%): we «剛剛» eat ok/agreed breakfast

**[3/23 11:02 AM] 閩南語只有台灣人會說** (H=1.58)
  Primary: «閩南» «語» «只有» Taiwan «人會» say/speak
  Alt (33%): «閩南» «語» «只有» Taiwan «人會» scold
  Alt (33%): «閩南» «語» «只有» Taiwan «人會» mean

**[3/23 4:18 PM] 沒今天忙** (H=1.85)
  Primary: [I, 36%] no/not today busy
  Alt (36%): [you, 36%] no/not today busy
  Alt (22%): [we, 22%] no/not today busy

**[3/23 7:04 PM] 吃晚飯** (H=1.85)
  Primary: [I, 36%] eat «晚» rice/meal
  Alt (36%): [you, 36%] eat «晚» rice/meal
  Alt (22%): [we, 22%] eat «晚» rice/meal

**[3/23 7:04 PM] 是的** (H=1.85)
  Primary: [I, 36%] is/am/are
  Alt (36%): [you, 36%] is/am/are
  Alt (22%): [we, 22%] is/am/are

**[3/23 7:04 PM] 可以煮湯也可以用炒的** (H=1.85)
  Primary: [I, 36%] «可以» cook «湯» «也» «可以» «用炒»
  Alt (36%): [you, 36%] «可以» cook «湯» «也» «可以» «用炒»
  Alt (22%): [we, 22%] «可以» cook «湯» «也» «可以» «用炒»

**[3/23 9:12 PM] 也很好吃** (H=1.85)
  Primary: [I, 36%] «也» «很» «好吃»
  Alt (36%): [you, 36%] «也» «很» «好吃»
  Alt (22%): [we, 22%] «也» «很» «好吃»

**[3/23 10:22 PM] 好的、謝謝你** (H=1.00)
  Primary: good «、» thank you you
  Alt (50%): ok/agreed «、» thank you you

### 3/24
**[3/24 11:22 AM] 剛剛一對夫妻按摩半小時好了** (H=2.00)
  Primary: «剛剛» «一對» «夫妻» «按摩» «半» «小» «時» good [completed]
  Alt (26%): «剛剛» «一對» «夫妻» «按摩» «半» «小» «時» ok/agreed [completed]
  Alt (24%): «剛剛» «一對» «夫妻» «按摩» «半» «小» «時» good [now/changed]

**[3/24 11:34 AM] 所以肯定要叫搬家公司幫忙拆好了，搬去另一個姐姐他們家在組裝上去、這些我們都不會用** (H=1.67)
  Primary: [you, 56%] «所以» «肯定» «要» «叫» «搬家» company help «拆好» [completed] «，» «搬去» «另» «一個» «姐姐» they «家» «在» «組裝» «上去» «、» «這些» we «都» not «會» «用»
  Alt (22%): [I, 22%] «所以» «肯定» «要» «叫» «搬家» company help «拆好» [completed] «，» «搬去» «另» «一個» «姐姐» they «家» «在» «組裝» «上去» «、» «這些» we «都» not «會» «用»
  Alt (17%): [we, 17%] «所以» «肯定» «要» «叫» «搬家» company help «拆好» [completed] «，» «搬去» «另» «一個» «姐姐» they «家» «在» «組裝» «上去» «、» «這些» we «都» not «會» «用»

**[3/24 11:34 AM] 要會拆下來、也要裝上去、還要搬得動，那都太重了，我們搬不動** (H=1.67)
  Primary: [you, 56%] «要» «會» «拆» «下來» «、» «也» «要» «裝» «上去» «、» «還要» «搬得» «動» «，» «那» «都» «太重» [completed] «，» we move «不動»
  Alt (22%): [I, 22%] «要» «會» «拆» «下來» «、» «也» «要» «裝» «上去» «、» «還要» «搬得» «動» «，» «那» «都» «太重» [completed] «，» we move «不動»
  Alt (17%): [we, 17%] «要» «會» «拆» «下來» «、» «也» «要» «裝» «上去» «、» «還要» «搬得» «動» «，» «那» «都» «太重» [completed] «，» we move «不動»

**[3/24 11:34 AM] 看不懂你的意思** (H=1.85)
  Primary: [I, 36%] «看不懂» you «意思»
  Alt (36%): [you, 36%] «看不懂» you «意思»
  Alt (22%): [we, 22%] «看不懂» you «意思»

**[3/24 11:34 AM] 你不是也受傷了，在治療、拿那些重的東西對你不適合、尤其我們是住在2樓，要從2樓搬下來，那實在太麻煩了、太吃力了** (H=1.58)
  Primary: you «不是» «也» «受傷» [completed] «，» «在» «治療» «、» «拿» «那些» «重» «東西» right/correct you not «適合» «、» «尤其» we is/am/are live «在» «2» «樓» «，» «要» «從» «2» «樓» move «下來» «，» «那» «實在» «太» «麻煩» [completed] «、» «太» «吃力» [completed]
  Alt (32%): you «不是» «也» «受傷» [now/changed] «，» «在» «治療» «、» «拿» «那些» «重» «東西» right/correct you not «適合» «、» «尤其» we is/am/are live «在» «2» «樓» «，» «要» «從» «2» «樓» move «下來» «，» «那» «實在» «太» «麻煩» [now/changed] «、» «太» «吃力» [now/changed]
  Alt (32%): you «不是» «也» «受傷» (too much) «，» «在» «治療» «、» «拿» «那些» «重» «東西» right/correct you not «適合» «、» «尤其» we is/am/are live «在» «2» «樓» «，» «要» «從» «2» «樓» move «下來» «，» «那» «實在» «太» «麻煩» (too much) «、» «太» «吃力» (too much)

**[3/24 1:24 PM] 不用表現** (H=1.85)
  Primary: [I, 36%] «不用» «表現»
  Alt (36%): [you, 36%] «不用» «表現»
  Alt (22%): [we, 22%] «不用» «表現»

**[3/24 1:24 PM] 是一對夫妻跟一個女兒、先生好像是外國、太太是大陸人、** (H=1.85)
  Primary: [I, 36%] is/am/are «一對» «夫妻» «跟» «一個» «女兒» «、» «先生» «好像» is/am/are «外國» «、» «太太» is/am/are «大» «陸人» «、»
  Alt (36%): [you, 36%] is/am/are «一對» «夫妻» «跟» «一個» «女兒» «、» «先生» «好像» is/am/are «外國» «、» «太太» is/am/are «大» «陸人» «、»
  Alt (22%): [we, 22%] is/am/are «一對» «夫妻» «跟» «一個» «女兒» «、» «先生» «好像» is/am/are «外國» «、» «太太» is/am/are «大» «陸人» «、»

**[3/24 1:24 PM] 你先帶看看自己感覺良好、才可以大家一起合夥、一起賺錢** (H=1.58)
  Primary: you «先» bring «看看» oneself «感覺» «良好» «、» «才» «可以» everyone «一起» «合» «夥» «、» «一起» «賺» money
  Alt (33%): you «先» wear «看看» oneself «感覺» «良好» «、» «才» «可以» everyone «一起» «合» «夥» «、» «一起» «賺» money
  Alt (33%): you «先» lead/guide «看看» oneself «感覺» «良好» «、» «才» «可以» everyone «一起» «合» «夥» «、» «一起» «賺» money

**[3/24 2:02 PM] 所以我才說錢慢慢賺、平安健康最重要** (H=1.58)
  Primary: «所以» I «才» say/speak money slowly/take your time «賺» «、» peace/safe healthy «最» important
  Alt (33%): «所以» I «才» scold money slowly/take your time «賺» «、» peace/safe healthy «最» important
  Alt (33%): «所以» I «才» mean money slowly/take your time «賺» «、» peace/safe healthy «最» important

**[3/24 2:22 PM] 好吃、健康** (H=1.85)
  Primary: [I, 36%] «好吃» «、» healthy
  Alt (36%): [you, 36%] «好吃» «、» healthy
  Alt (22%): [we, 22%] «好吃» «、» healthy

**[3/24 2:22 PM] 這個說的是同事或者是朋友** (H=1.58)
  Primary: «這個» say/speak is/am/are coworker «或者» is/am/are friend
  Alt (33%): «這個» scold is/am/are coworker «或者» is/am/are friend
  Alt (33%): «這個» mean is/am/are coworker «或者» is/am/are friend

**[3/24 2:22 PM] 人生在世、一些好朋友是好事** (H=1.00)
  Primary: «人生在世» «、» «一些» good friend is/am/are «好事»
  Alt (50%): «人生在世» «、» «一些» ok/agreed friend is/am/are «好事»

**[3/24 2:39 PM] 好的小心慢慢開車** (H=1.00)
  Primary: good be careful slowly/take your time drive
  Alt (50%): ok/agreed be careful slowly/take your time drive

**[3/24 8:45 PM] 那回家都凌晨了** (H=1.58)
  Primary: «那» «回家» «都» «凌晨» [completed]
  Alt (32%): «那» «回家» «都» «凌晨» [now/changed]
  Alt (32%): «那» «回家» «都» «凌晨» (too much)

**[3/24 8:45 PM] 好的小心慢慢開車** (H=1.00)
  Primary: good be careful slowly/take your time drive
  Alt (50%): ok/agreed be careful slowly/take your time drive

**[3/24 9:36 PM] 我們到老闆娘她家了** (H=2.00)
  Primary: we arrive «老» «闆» «娘» «她家» [completed]
  Alt (26%): we succeed «老» «闆» «娘» «她家» [completed]
  Alt (24%): we arrive «老» «闆» «娘» «她家» [now/changed]

**[3/24 9:36 PM] 我在帶你們大家去吃抹茶拉麵** (H=1.58)
  Primary: I «在» bring you all everyone go eat «抹» «茶» «拉» «麵»
  Alt (33%): I «在» wear you all everyone go eat «抹» «茶» «拉» «麵»
  Alt (33%): I «在» lead/guide you all everyone go eat «抹» «茶» «拉» «麵»

**[3/24 9:36 PM] 現在的社會千萬不要做吃的不好賺、又很辛苦、又浪費時間** (H=1.58)
  Primary: now «社會» «千萬» «不要» do/make eat «不好» «賺» «、» «又» «很» hard/difficult «、» «又» «浪費» time
  Alt (33%): now «社會» «千萬» «不要» work_as eat «不好» «賺» «、» «又» «很» hard/difficult «、» «又» «浪費» time
  Alt (33%): now «社會» «千萬» «不要» conduct eat «不好» «賺» «、» «又» «很» hard/difficult «、» «又» «浪費» time

**[3/24 11:15 PM] 檢查血紅素不夠、貧血住院、檢查出來是攝護腺癌第四期、才出院回家、** (H=1.85)
  Primary: [I, 36%] «檢» «查血» «紅素» «不夠» «、» «貧血» «住院» «、» «檢» «查出» come is/am/are «攝護» «腺癌» «第四期» «、» «才» «出院» «回家» «、»
  Alt (36%): [you, 36%] «檢» «查血» «紅素» «不夠» «、» «貧血» «住院» «、» «檢» «查出» come is/am/are «攝護» «腺癌» «第四期» «、» «才» «出院» «回家» «、»
  Alt (22%): [we, 22%] «檢» «查血» «紅素» «不夠» «、» «貧血» «住院» «、» «檢» «查出» come is/am/are «攝護» «腺癌» «第四期» «、» «才» «出院» «回家» «、»

**[3/24 11:15 PM] 已經出院、星期一到星期五要去醫院電療、** (H=1.00)
  Primary: «已經» «出院» «、» «星期一» arrive «星期五» «要» go «醫院» «電療» «、»
  Alt (50%): «已經» «出院» «、» «星期一» succeed «星期五» «要» go «醫院» «電療» «、»

**[3/24 11:15 PM] 沒事、謝謝你** (H=1.85)
  Primary: [I, 36%] it's nothing/no problem «、» thank you you
  Alt (36%): [you, 36%] it's nothing/no problem «、» thank you you
  Alt (22%): [we, 22%] it's nothing/no problem «、» thank you you

**[3/24 11:15 PM] 小寶寶、去幫我爸爸賣了一天** (H=1.58)
  Primary: «小寶寶» «、» go help I dad sell [completed] «一天»
  Alt (32%): «小寶寶» «、» go help I dad sell [now/changed] «一天»
  Alt (32%): «小寶寶» «、» go help I dad sell (too much) «一天»

**[3/24 11:15 PM] 心中有佛、什麼都好** (H=1.00)
  Primary: «心中» «有佛» «、» «什麼» «都» good
  Alt (50%): «心中» «有佛» «、» «什麼» «都» ok/agreed

### 3/25
**[3/25 10:52 AM] 好的、謝謝你** (H=1.00)
  Primary: good «、» thank you you
  Alt (50%): ok/agreed «、» thank you you

**[3/25 7:54 PM] 我先去忙，晚點說** (H=1.58)
  Primary: I «先» go busy «，» «晚點» say/speak
  Alt (33%): I «先» go busy «，» «晚點» scold
  Alt (33%): I «先» go busy «，» «晚點» mean

**[3/25 10:28 PM] 大家都很好、謝謝你的關心** (H=1.00)
  Primary: everyone «都» «很» good «、» thank you you «關心»
  Alt (50%): everyone «都» «很» ok/agreed «、» thank you you «關心»

**[3/25 10:28 PM] 你是說你租房子是在賓州** (H=1.58)
  Primary: you is/am/are say/speak you «租房子» is/am/are «在» «賓州»
  Alt (33%): you is/am/are scold you «租房子» is/am/are «在» «賓州»
  Alt (33%): you is/am/are mean you «租房子» is/am/are «在» «賓州»

**[3/25 10:28 PM] 就是你說的每個月1900房租，是嗎？** (H=2.00)
  Primary: «就是» you say/speak «每個» «月» «1900» rent «，» is/am/are «？»
  Alt (25%): «就是» you scold «每個» «月» «1900» rent «，» is/am/are «？»
  Alt (25%): «就是» you mean «每個» «月» «1900» rent «，» is/am/are «？»

### 3/26
**[3/26 9:33 AM] 吃早餐** (H=1.85)
  Primary: [I, 36%] eat breakfast
  Alt (36%): [you, 36%] eat breakfast
  Alt (22%): [we, 22%] eat breakfast
