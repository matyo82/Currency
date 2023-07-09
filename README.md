# Saving the price of dollars in Rials
___
## Getting started guide
## step one
+ First, create a database and put its information in a file called dataItem.py
>Table columns include:
>> + id = type: int primary kay AUTO_INCREMENT
>> + name = varchar(60) unique
>> + price = int(6)

## step tow
> ### run main.py
>> ####  commands:
>> 1. `update`: update list in database
>> 2. `show-price`: Display all rows in the table

______
# ذخیره قیمت ارز ها در پایگاه داده
#### این اسکریپت ابتدا از سایت جداولی را خوانده و آن را تفکیک میکند. سپس ان را داخل یک جدول در دیتا بیس قرار میدهد.
در کامیت های قبلی میتوانید لیست ارز ها همراه با قیمت را در یک فایل csv قرار دهید
#### راهنمای استقاده از برنامه:
> 1. ابتدا یک دیتا بیس و یک جدول بسازید و اطلاعات ان را داخل فایلی با نام زیر قرار دهید:
>> dataItem.py
> 2. در جدول سه ستون وجود دارد که همراه با ویژگی در زیر برای شما نمایش گزاشته شده است:
>> + id = type: int primary kay AUTO_INCREMENT
>> + name = varchar(60) unique
>> + price = int(6)
> 3. فایل اصلی را اجرا کنید و کامند مورد نظر را وارد کنید
>> 1. `update`:
>>  تمامی لیست ها را داخل پایگاه داده به روز رسانی میکند
>> 2. `show-price`:
>> تمامی ردیف های موجود را داخل تریمنال نمایش میدهد 