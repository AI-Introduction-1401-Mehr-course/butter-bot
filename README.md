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
    {replace this line with output of: `git log --pretty="%h %aN '%s'"` but DONT COMMIT THE REPLACEMENT; hard coding dynamic data is redundant.}
```