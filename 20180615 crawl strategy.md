# 크롤링 방법

## ID 규칙

- 제품 리스트에서의 product id 확인
- json['object']['shopprd']['list'][idx]['v_productcd']P00003858

## 제품 리스트

- URL : http://www.amorepacificmall.com/mobile/shop/mobile_shop_category_product_list_ajax.do

- method : POST

- data : form-data

- form :
    - i_iNowPageNo: 1
    - i_sCategorycd1: CTG001
    - i_sCategorycd1_dict = {'CTG001':'스킨케어', 'CTG002':'메이크업', 'CTG003':'네일&향수', 'CTG004':'데일리뷰티', 'CTG005':'소품&도구', 'CTG006':'뷰티푸드', 'CTG007':'옴므', 'CTG110':'베이비'=}
    - i_sBrandcd = {'AEK':'설화수', 'AFK':'헤라','MCK':'프리메라','아모레퍼시픽':'AOK','리리코스':'AMK','아이오페':'AGK','라네즈':'ADK','마몽드':'AHK','한율':'MKK','베리떼':'AKK','려':'MRK','':''}
- response : json

```json
{
    "status": "succ",
    "message": "",
    "object": {
        "shopprd": {
            "cnt": {
                "n_recordcnt": 1105
            },
            "list": [
                {
                    "n_wish_cnt": 333,
                    "v_typecd": "0001",
                    "v_productcd": "P00003858",
                    "v_feature_tag": "DG_P010,1+1,FEATURE",
                    "n_text_cnt": 15281,
                    "v_flag_list_price_beauty": "Y",
                    "n_single_point": 4.5,
                    "v_flag_price_prm": "Y",
                    "n_plus_evt_give_cnt": 1,
                    "v_prod_ctg_path": "스킨케어>스페셜 케어>마스크 & 팩",
                    "n_option_cnt": 6,
                    "n_stockqty": 0,
                    "v_comment": "발효 공법이 더해진 플라워 성분이 피부에 영양분을 촘촘하고 빠르게 전달해주는 초밀착 마스크",
                    "v_nickname": "발효 공법이 더해진 플라워 성분이 피부에 영양분을 촘촘하고 빠르게 전달해주는 초밀착 마스크",
                    "func_": "",
                    "v_img_path_155": "http://images.amorepacificmall.com/UPLOAD/UPLOAD_IMAGE/C026/20180400/IMG1514POw254889063_155.jpg",
                    "v_flag_price_beauty": "Y",
                    "v_optionnm": "[NEW]연꽃 마스크-진정",
                    "v_img_path_356": "http://images.amorepacificmall.com/UPLOAD/UPLOAD_IMAGE/C026/20180400/IMG1514POw254889063_356.jpg",
                    "v_flag_list_price_member": "Y",
                    "n_num": 1,
                    "v_flag_giftcard_enable": "N",
                    "n_price": 1500,
                    "list_func_": "",
                    "v_flag_price_member": "Y",
                    "v_flag_reser_real": "N",
                    "v_brandnm": "마몽드",
                    "v_flag_list_price_prm": "Y",
                    "v_optioncd": "110650149",
                    "v_flag_upto": "N",
                    "v_productnm_en": "FLOWER Essence Mask",
                    "n_vote_cnt": 114,
                    "v_categorycd": "CTG001",
                    "v_list_price_typecd": "PR01",
                    "v_img_path": "http://images.amorepacificmall.com/UPLOAD/UPLOAD_IMAGE/C026/20180400/IMG1514POw254889063_155.jpg",
                    "n_photo_cnt": 113,
                    "n_opt_spf": 0,
                    "n_sort": 1213,
                    "v_flag_price_gift": "Y",
                    "n_list_price": 1500,
                    "v_brandcd": "AHK",
                    "n_plus_evt_buy_cnt": 1,
                    "v_flag_solopack": "N",
                    "v_flag_list_price_point": "Y",
                    "v_productnm": "플라워 에센스 마스크",
                    "v_flag_beauty": "N",
                    "v_reg_dtm": "20140129092721",
                    "v_img_ssl_path_155": "https://images.amorepacificmall.com/UPLOAD/UPLOAD_IMAGE/C026/20180400/IMG1514POw254889063_155.jpg",
                    "v_flag_price_point": "Y",
                    "n_review_cnt": 15384,
                    "v_gift_card_maxvalue": 0,
                    "v_price_typecd": "PR01",
                    "v_img_path_0": "http://images.amorepacificmall.com/UPLOAD/UPLOAD_IMAGE/C026/201712/IMG1514POw254889063.jpg",
                    "v_statuscd": "0002",
                    "v_flag_list_price_gift": "Y",
                    "v_delivery_typecd": "0001"
                }
            ]
            "page": {
                "i_iPageSize": "30",
                "i_iRecordCnt": "1105",
                "i_iTotalPageCnt": "37",
                "i_iNowPageNo": "1",
                "i_iEndRownum": "30",
                "i_iPrevPage": "1",
                "i_iNextPage": "11",
                "i_iEndPage": "10",
                "i_iStartRownum": "1",
                "i_iStartPage": "1"
            }
        }
    }
}
```

## 모바일 포토리뷰

- URL : http://www.amorepacificmall.com/mobile/shop/mobile_shop_product_review_ajax.do

- method : POST

- data : form-data

- form : 
    - i_sProductcd (상품코드 예:SPR20150313000007801)
    - i_sTypecd (리뷰타입 0001)
    - i_iNowPageNo (페이지 예:1)

- response : json

```json
{
    "status": "succ",
    "message": "",
    "object": {
        "textReview": {
            "imgList": { ... },
            "reqVo": { ... },
            "recordCnt": 49,
            "list": [
                {
                    "n_view_cnt": 2,
                    "v_flag_agree": "Y",
                    "n_reply_cnt": 1,
                    "v_typecd": "0001",
                    "v_cmt_levelnm": "쌩얼",
                    "v_productcd": "SPR20150313000007801",
                    "v_reg_channel": "APP",
                    "v_userid": "amiberry",
                    "n_option_cnt": 1,
                    "v_nickname": "쭈쭈언니",
                    "v_reg_userid": "amiberry",
                    "v_levelcd": "LV16",
                    "v_optionnm": "굿모닝 마일드 클렌저_17",
                    "n_vote_total": 0,
                    "v_clob": "[image#01] 너무 굿딜이라 쟁여둔 세안제 많은데 한 번 사봤어요. 아침마다 이거 쓰는데 진짜 각질 걱정이 없네요. 포인트는 마른 얼굴에 먼저 문지르는 거에요. 이렇게 좋은 건줄 알았음 여러 개 더 사둘 걸 그랬어요. 이거 정착템 될 듯요.",
                    "v_update_type": "ADMIN",
                    "v_cmt_levelcd": "CZ_L001",
                    "v_reg_type": "USER",
                    "n_recom_point": 1,
                    "n_num": 1,
                    "v_langcd": "ko",
                    "n_bprofile": 0,
                    "n_vote_cnt": 0,
                    "n_use_point": 1,
                    "v_flag_rebuy": "N",
                    "v_rv_typenm": "구매후기",
                    "n_photo_cnt": 0,
                    "n_user_vote": 0,
                    "v_flag_best": "N",
                    "v_title": "이거 진짜 완소템이네요.",
                    "v_update_dtm": "20180615110844",
                    "v_tagnm": "피부(Skin)",
                    "v_sitecd": "CMC",
                    "v_update_userid": "AC919074",
                    "v_product_typecd": "0001",
                    "v_proimag_url": "http://images.amorepacificmall.com/UPLOAD/UPLOAD_IMAGE/CMC/USR_PHOTO/201806/IMG1528XWY123145726_128.jpg",
                    "v_reviewcd": "CRV20180615000933599",
                    "v_typenm": "이미지",
                    "v_ordercd": "A180610005768128",
                    "n_vote_plus_cnt": 0,
                    "v_reg_dtm": "20180615025939",
                    "v_rv_typecd": "DC_T005",
                    "v_flag_prebuy": "N",
                    "n_levelno": "6",
                    "v_levelnm": "VVIP+",
                    "n_cmt_levelno": "1"
                },
            ]
            "recordInfo": {
                "n_recom_point_1": 14,
                "n_recom_point_2": 34,
                "photo_count": 49,
                "n_recom_point_3": 153,
                "n_recom_point_4": 481,
                "n_recom_point_5": 1290,
                "n_recordcnt": 49,
                "text_count": 1973
            },
            "page": {
                "i_iPageSize": "10",
                "i_iRecordCnt": "49", // 개수
                "i_iTotalPageCnt": "5", // 페이지 수
                "i_iNowPageNo": "1",
                "i_iEndRownum": "10",
                "i_iPrevPage": "1",
                "i_iNextPage": "5",
                "i_iEndPage": "5",
                "i_iStartRownum": "1",
                "i_iStartPage": "1"
            }
        }
    }
}
```

## 모바일 일반리뷰

- URL : http://www.amorepacificmall.com/mobile/shop/mobile_shop_product_review_ajax.do

- method : POST

- data : form-data

- form : 
    - i_sProductcd (상품코드 예:SPR20150313000007801)
    - i_sTypecd (리뷰타입 0004)
    - i_iNowPageNo (페이지 예:1)

- response : json

기본 구조는 포토리뷰와 동일.
```json
{
    "n_view_cnt": 0,
    "n_reply_cnt": 0,
    "v_typecd": "0004",
    "v_cmt_levelnm": "쌩얼",
    "v_productcd": "SPR20150313000007801",
    "v_reg_channel": "MOBILE", // 리뷰 작성 채널
    "v_userid": "syury83",
    "n_option_cnt": 1,
    "v_reg_userid": "syury83",
    "v_levelcd": "LV11",
    "v_optionnm": "굿모닝 마일드 클렌저_17",
    "n_vote_total": 0,
    "v_update_type": "USER",
    "v_cmt_levelcd": "CZ_L001",
    "v_reg_type": "USER",
    "n_recom_point": 1, // 추천 점수
    "v_content": "별로에요 씻은느낌도없고 사용하다 말았어요ㅡ\n재구매의사는 없어요", // 리뷰 내용
    "v_eventcd": "TEXT_REVIEW_1ST",
    "n_num": 1,
    "v_langcd": "ko",
    "n_bprofile": 0,
    "n_vote_cnt": 0,
    "n_use_point": 0,
    "v_flag_rebuy": "N",
    "n_photo_cnt": 0,
    "n_user_vote": 0,
    "v_flag_best": "N",
    "v_update_dtm": "20180615142213",
    "v_sitecd": "CMC",
    "v_update_userid": "syury83",
    "v_product_typecd": "0001",
    "v_reviewcd": "CRV20180615000934021",
    "v_typenm": "텍스트리뷰",
    "v_ordercd": "A180415004334640",
    "n_vote_plus_cnt": 0,
    "v_reg_dtm": "20180615142213",
    "v_flag_prebuy": "N",
    "n_levelno": "1",
    "v_levelnm": "WELCOME", // 사용자 레벨
    "n_cmt_levelno": "1"
},
```