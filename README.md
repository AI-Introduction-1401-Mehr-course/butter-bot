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

### bfs:

همه حالات همسایه رو به یه صف اضافه میکنه که به ترتیب ورود اعضاش اکسپلور میشن تا وقتی که یه جواب پیدا کنه و برش گردونه.

### ids:

دی اف اسو با عمق محدود اجرا میکنه و مدام عمقو زیاد میکنه تا سطحی ترین جوابو پیدا کنه.

### ucs:

همه حالات همسایه رو به یه لیست اضافه میکنه و لیست رو بر اساس هزینه از کم به زیاد مرتب میکنه و کم هزینه ترین رو اکسپلور میکنه.

## A*:

همه حالات همسایه رو به یه لیست اضافه میکنه و لیست رو بر اساس مجموع هزینه و مقدار تابع هیوریستیک از کم به زیاد مرتب میکنه و عضوی رو که کمترین مجموع رو داره اکسپلور میکنه.

## best first search (greedy):

همه حالات همسایه رو به یه لیست اضافه میکنه و لیست رو بر اساس مقدار تابع هیوریستیک از کم به زیاد مرتب میکنه و عضوی رو که کمترین مقدار رو اکسپلور میکنه.

## توابع هیوریستیک

### جمع حداقل هزینه هل دادن یک کره به هر خانه هدف:

حداقل هزینه رسیدن از هر خانه هدف به بقیه مختصات جدولو حساب میکنه و بعد برای هر کدوم مقرون به صرفه ترین کررو انتخاب میکنه و در نهایت همشو جمع میکنه و بر میگردونه.

### (other heuristics placeholder)