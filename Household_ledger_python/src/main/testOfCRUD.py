'''
Created on 2021. 7. 22.

sqliteCRUD Test

@author: pc356
'''

from main import HL_CRUD

if __name__ == '__main__':
    # # table 만들기
    HL_CRUD.createTable()
    #
    # # 자료 하나 입력하기
    HL_CRUD.insertData('2021-08-02', '수입', '수입_급여', '2000000', '', '07월 급여')
    #
    # # 여러 자료를 동시에 입력하기
    # t_data = (
    #     ('ygs','유관순','1234','삼월하늘'),
    #     ('lss','이순신','1234','한산섬'),
    #     ('ysd','윤선도','1234','지국총')
    # )
    # sqliteCRUD.insertManyData(t_data)
    #
    # sqliteCRUD.selectAll()
    # sqliteCRUD.select('hgd')
    # sqliteCRUD.update(('홍길동','1237','동서번쩍','hgd')) # update시 질의문의 물음표 순서에 맞추어 tuple 형식으로 작성할 것!
    # sqliteCRUD.delete('hgd')