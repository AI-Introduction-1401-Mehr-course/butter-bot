<div style="direction: rtl;">

# ربات کره

## فضای حالت ربات کره

فضای حالت با سه تابع Action, Resultو Cost تعریف شده؛ همچنین یک شمارنده شامل تمام حرکات ممکن(ابر مجموعه حرکات ممکن در تمام حالات ممکن) و تابع هدف که مشخص میکند، حالت فعلی عضو هدف هست یا نه [به خاطر ساده شدن کد] داخل همین کلاس پیاده سازی شدن.

### تابع حرکات ممکن:

تمام حرکات ممکن روی وضعیت فعلی اعمال میشنو اونایی که منجر به وضعیت هایی میشن که توی فضای حالت موجودنو بر میگردونه.

### تابع نتیجه حرکت:

تابع نتیجه حرکت با گرفتن یک حرکت و اعمال کردنش روی حالت فعلی، حالت مقصدو بر میگردونه. فرض بر اینه که حرکت ورودی، منجر به یه وضع موجود توی فضای حالت میشه.

### تابع هزینه حرکت:

هزینه اعمال حرکت ورودیو روی وضع فعلی بر میگردونه. مثل تابع قبل، انتظار میره که حرکت ورودی به وضع موجود توی فضای حالت منجر بشه.

## الگوریتم های جستجو

### dfs:

به صورت بازگشتی خودشو با همه اکشنای ممکن وضعیت فعلی صدا میزنه و هر کدوم که بتونن جوابو پیدا کنن بر میگردونه.

پیچیدگی زمانی: O(b^m)   [b = ضریب انشعاب , m = حداکثر عمق]

پیچیدگی فضایی: O(b*m)   [b = ضریب انشعاب , m = حداکثر عمق]

### bfs:

همه حالات همسایه رو به یه صف اضافه میکنه که به ترتیب ورود اعضاش اکسپلور میشن تا وقتی که یه جواب پیدا کنه و برش گردونه.

پیچیدگی زمانی: O(b^d)   [b = ضریب انشعاب , d = عمق استیت هدف]

پیچیدگی فضایی: O(b^d)   [b = ضریب انشعاب , d = عمق استیت هدف]

### ids:

دی اف اسو با عمق محدود اجرا میکنه و مدام عمقو زیاد میکنه تا سطحی ترین جوابو پیدا کنه.

پیچیدگی زمانی: O(b^d)   [b = ضریب انشعاب , d = عمق استیت هدف]

پیچیدگی فضایی: O(b*d)   [b = ضریب انشعاب , d = عمق استیت هدف]

### ucs:

همه حالات همسایه رو به یه لیست اضافه میکنه و لیست رو بر اساس هزینه از کم به زیاد مرتب میکنه و کم هزینه ترین رو اکسپلور میکنه.

پیچیدگی زمانی: O(b^(1+C/ε))   [b = ضریب انشعاب , C = هزینه مسیر بهینه , ε = حداقل هزینه یک حرکت]

پیچیدگی فضایی: O(b^(1+C/ε))   [b = ضریب انشعاب , C = هزینه مسیر بهینه , ε = حداقل هزینه یک حرکت]

### A*:

همه حالات همسایه رو به یه لیست اضافه میکنه و لیست رو بر اساس مجموع هزینه و مقدار تابع هیوریستیک از کم به زیاد مرتب میکنه و عضوی رو که کمترین مجموع رو داره اکسپلور میکنه.

پیچیدگی زمانی: O(b^d)   [b = ضریب انشعاب , d = عمق استیت هدف]

پیچیدگی فضایی: O(b^d)   [b = ضریب انشعاب , d = عمق استیت هدف]

### best first search (greedy):

همه حالات همسایه رو به یه لیست اضافه میکنه و لیست رو بر اساس مقدار تابع هیوریستیک از کم به زیاد مرتب میکنه و عضوی رو که کمترین مقدار رو اکسپلور میکنه.

پیچیدگی زمانی: O(b^m)   [b = ضریب انشعاب , m = حداکثر عمق]

پیچیدگی فضایی: O(b^m)   [b = ضریب انشعاب , m = حداکثر عمق]

## توابع هیوریستیک

### جمع فاصله ربات تا نزدیک ترین کره ای که به هدف نزدیک است و فاصله آن کره تا نزدیک ترین هدف (alpha):

با توجه به موقعیت ربات نزدیک ترین کره رو پیدا میکنه (اگر فاصله ربات با 2 تا کره برابر باشه کره ای رو در نظر میگیره که به یک هدف نزدیک تره) و فاصله ی ربات تا اون کره رو با فاصله ی اون کره تا نزدیک ترین هدف جمع میکنه و برمیگردونه.

پیچیدگی زمانی: O(len(butter_cells) + len(target_cells))

پیچیدگی فضایی: O(len(butter_cells) + len(target_cells))

### تعداد خانه های هدفی که کره ای داخل انها قرار نگرفته (beta):

تعداد هدف هایی که مختصاتشون با مختصات هیج کره ای برابر نیست رو حساب میکنه و برمیگردونه.

پیچیدگی زمانی: O(len(target_cells))

پیچیدگی فضایی: O(len(target_cells))

### جمع حداقل هزینه هل دادن یک کره به هر خانه هدف (gamma):

حداقل هزینه رسیدن از هر خانه هدف به بقیه مختصات جدولو حساب میکنه و بعد برای هر کدوم مقرون به صرفه ترین کررو انتخاب میکنه و در نهایت همشو جمع میکنه و بر میگردونه.

پیچیدگی زمانی: O(rows\*columns\*len(target_cells)\*len(butter_cells))

پیچیدگی فضایی: O(rows\*columns\*len(target_cells))

###  جمع حداقل هزینه هل دادن یک کره به هر خانه هدف و هزینه رسیدن به یک ربات کره (delta):

خروجی گاما رو با هزینه رسیدن به نزدیک ترین کره جمع میکنه و بر میگردونه.

پیچیدگی زمانی: O(rows\*columns\*len(target_cells)\*len(butter_cells))

پیچیدگی فضایی: O(rows\*columns\*len(target_cells))

### جمع فاصله ربات تا نزدیک ترین کره و فاصله آن کره تا نزدیک ترین هدف:

با توجه به موقعیت ربات نزدیک ترین کره رو پیدا میکنه و فاصله ی ربات تا اون کره رو با فاصله ی اون کره تا نزدیک ترین هدف جمع میکنه و برمیگردونه.

پیچیدگی زمانی: O(len(butter_cells) + len(target_cells))

پیچیدگی فضایی: O(len(butter_cells) + len(target_cells))

### تعداد کره هایی که به هدف نرسیده اند:

تعداد کره هایی که مختصاتشون با مختصات هیج هدفی برابر نیست رو حساب میکنه و برمیگردونه.

پیچیدگی زمانی: O(len(butter_cells))

پیچیدگی فضایی: O(len(butter_cells))

## راهنمای ابزار خط فرمان:

</div>
<div >

```text
usage: run.py [-h] [-i INPUT_FILE] [-s SEARCH_ALGORITHM] [-e HEURISTIC_FUNCTION] [-t TIMEOUT]

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                        read from file instead of stdin
  -s SEARCH_ALGORITHM, --search-algorithm SEARCH_ALGORITHM
                        algorithm for executing search
  -e HEURISTIC_FUNCTION, --heuristic-function HEURISTIC_FUNCTION
                        heuristic for informed searchs
  -t TIMEOUT, --timeout TIMEOUT
                        time limit of search execution
```

</div>
<div style="direction: rtl;">

## تاریخچه کامیت ها:

</div>
<div >

```text
  f8f78b9 Nima Shadman 'Format With Black'
  9b5cf7d Nima Shadman 'Keep Track of Visited Nodes in BFS,UCS,A*,Greedy'
  33df5d4 Mohammad Karami 'Add delta heuristic docstring and documentation'
  4d13bb9 Mohammad Karami 'Reimplement dfs without recursion'
  6babe90 Nima Shadman 'Added new testcase'
  edfc88d Nima Shadman 'Added Space Complexity of My Heuristics'
  5cfdc6a Nima Shadman 'modified main.py'
  8ff5d46 Nima Shadman 'Added Time And Space Complexity of IDS'
  ac30496 Nima Shadman 'Added Time And Space Complexity of BFS'
  314f6ad Nima Shadman 'Changed heuristic function default to beta'
  dd343a1 Nima Shadman 'Changed timeout default to 3'
  726fdcd Nima Shadman 'Added Time And Space Complexity of DFS'
  5fb8b08 Nima Shadman 'Added Space Complexity of UCS,A*,Greedy'
  78e4216 Nima Shadman 'Added Time Complexity of UCS,A*,Greedy'
  82228a0 Nima Shadman 'Added Time Complexity of My Heuristics'
  c2e76e9 Mohammad Karami 'Improve command tool help'
  e40c00a Mohammad Karami 'Add 3 new tests'
  b158fa1 Mohammad Karami 'Add styling to readme'
  c2ba322 Mohammad Karami 'Add command line help to readme'
  6f55aaf Nima Shadman 'Added New Heuristic'
  7089131 Mohammad Karami 'Add time complexity of my heuristics'
  cfaa88d Mohammad Karami 'Initialize command line tool'
  3db5c81 Mohammad Karami 'Pick five heuristics and export them as greek letters'
  8db2957 Mohammad Karami 'Add commit history to doc'
  41f34fd Nima Shadman 'Added Heuristic Explainations to Doc'
  9908fc6 Nima Shadman 'Added UCS & A* & Greedy Explaination to Doc'
  da7cb52 Mohammad Karami 'Complete state space doc'
  95ecd5f Mohammad Karami 'Add new relaxed problem heuristic:  - min_of_total_cost_of_filling_target_cells_with_butter'
  b69088d Mohammad Karami 'Add performance tester script'
  2d1e07d Mohammad Karami 'Expect unsolvable problems'
  ec346b2 Mohammad Karami 'Initial documentation commit'
  33a25dc Mohammad Karami 'Implement new heuristics: - number_of_targets_with_no_butter - sum_of_min_cost_of_filling_target_cells_with_butter'     
  29c91b1 Mohammad Karami 'Change bloacked cells special value in cost_table'
  93c4aad Nima Shadman 'Added docstring'
  44fa5b3 Nima Shadman 'added new heuristic functions'
  7cc809d Mohammad Karami 'Add serialization'
  34328a6 Mohammad Karami 'Write docstring for: - butter bot state space - bfs - dfs - ids'
  fb1d3de Mohammad Karami 'Sort imports using isort'
  80d2510 Mohammad Karami 'Move heuristic out of use case'
  3d9407d Mohammad Karami 'Update file structure'
  2c002a9 Nima Shadman 'Merge branches 'main' and 'main' of https://github.com/AI-Introduction-1401-Mehr-course/butter-bot'
  12e3b1c Nima Shadman 'Added Heuristic Function'
  94f1dd6 Mohammad Karami 'Expect python versions older than 3.11'
  93d462a Nima Shadman 'Format With Black'
  1bd5f93 Nima Shadman 'Implement BestFirstSearch'
  1e77cb0 Nima Shadman 'Implement AStar'
  9878ed9 Nima Shadman 'Implement UCS'
  e2f7bef Mohammad Karami 'DFS and IDS implementation'
  ce90eb1 Mohammad Karami 'Implement breadth-first search'
  caa0e2d Mohammad Karami 'Add is_goal method to StateSpace'
  6af5537 Mohammad Karami 'Fix indexing error'
  2c55110 Mohammad Karami 'Make main.py and test state space initialization'
  17a71c6 Mohammad Karami 'Format with black'
  425b8f6 Mohammad Karami 'State space initial commit'
  3ba6d2d Mohammad Karami 'first commit'
```