from pprint import pprint
import re
import csv
import pyexcel

missing = ['']
contact_list = []

subst = r"+7(\2)\3-\4-\5"
subst1 = r"+7(\2)\3-\4-\5 \6\7"
pattern = re.compile(r"(\+7|8)(\d{3})(\d{3})(\d{2})(\d{2}$)")
pattern1 = re.compile(r"(\+7|8)?\s*(\d{3})(\d{3})(\d{2})(\d{2})(\D+)(\d+)")

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    for row in contacts_list:
        list_phone = []
        if row[0] not in missing:
            fam1 = row[0].split()
            for i in fam1:
                list_phone.append(i)


        if row[1] not in missing:
            fam2 = row[1].split()
            for i in fam2:
                list_phone.append(i)


        if row[2] not in missing:
            fam3 = row[2]
            list_phone.append(fam3)


        res = re.sub(r'[()-]', '', row[5])
        cleaned_res = re.sub(r'\s+', '', res)

        if pattern.search(cleaned_res):
            result = re.sub(pattern, subst, cleaned_res)
            list_phone.append(result)

        elif pattern1.search(cleaned_res):
            result1 = re.sub(pattern1, subst1, cleaned_res)
            if result1 == result:
                continue
            list_phone.append(result1)

        else:
            result = cleaned_res
            list_phone.append(result)

        contact_list.append(list_phone)

pyexcel.save_as(array = contact_list, dest_file_name = 'phonebook.csv')


