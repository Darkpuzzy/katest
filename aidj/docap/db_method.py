import pandas as pd
from .models import InFileData


# file = 'D:/projects/exdb/aidj/exfile/_РВ_2021_06_18_ТНГ-21-СМР-223_КОД.xlsx'

# Печатаем название листов в данном файле
# df = pd.read_excel(file)


class PyExcel:

    @classmethod
    def go_to_db(cls, file_to, file_id):
        date_frame = pd.read_excel(file_to)
        file_id = file_id
        test_list = []
        for item in date_frame.iloc[13:, 0:28].values:
            if str(item[0]) == 'nan':
                print('Nan')
            else:
                f = list(item)
                f.append(file_id)
                for i in f:
                    if str(i) == 'nan':
                        ind = f.index(i)
                        f[ind] = 0
                test_list.append(f)
        return cls.__apend_to_db(list_add=test_list)

    @classmethod
    def __apend_to_db(cls, list_add):
        try:
            for item in list_add:
                model = InFileData(number_raw=item[0],
                                   cryptcode=item[1],
                                   fsnb=item[2],
                                   mtr=item[3],
                                   metric=item[4],
                                   all_counts=item[5],
                                   price_not_nds=item[6],
                                   index=item[7],
                                   price_smeta=item[8],
                                   nomenclature=item[9],
                                   razdel=item[10],
                                   mtr_count=item[11],
                                   price_mtr_for_ed=item[12],
                                   price_mtr_sum=item[13],
                                   materials_price_mtr_sum=item[14],
                                   oborud=item[15],
                                   mtr_count_other=item[16],
                                   price_mtr_for_ed_other=item[17],
                                   price_mtr_sum_other=item[18],
                                   materials_price_mtr_sum_other=item[19],
                                   oborud_other=item[20],
                                   mtr_count_orders=item[21],
                                   price_mtr_for_ed_orders=item[22],
                                   price_mtr_sum_orders=item[23],
                                   materials_price_mtr_sum_orders=item[24],
                                   oborud_orders=item[25],
                                   operator=item[26],
                                   origin_mtr=item[27],
                                   original_file_id=item[28])
                model.save()
                print('Success')
            return {'Success'}
        except Exception as e:
            return {str(e)}

# print(PyExcel.go_to_db(file_to=file, file_id=1))
