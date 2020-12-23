from dynamic_programming import fibonacci as f
import pytest

FIB_5 = 5

FIB_100 = 354224848179261915075

FIB_1000 = '''
4346655768693745643568852767504062580
2564660517371780402481729089536555417
9490518904038798400792551692959225930
8032263477520968962323987332247116164
2996440906533187938298969649928516003
704476137795166849228875
'''

FIB_10000 = '''
3364476487643178326662161200510754331030
2148460680063906564769974680081442166662
3681555955136337340255820653326808361593
7373479048386526826304089246305643188735
4544369559827491606602099884183933864652
7313000888302692356736131351175792974378
5441375213052050434770160226475831890652
7890855154366159582987279682987510631200
5754287834532155151038708182989697916131
2785626503319548714021428753269818796204
6936097879900350962302291026368131493195
2756302278376284415403605844025721143349
6118002309120828704608892396232883546150
5776583271252546093591128203925285393434
6209042452489294039017062338889910858410
6518317336043747073790855263176432573399
3712871937587746897479926305837065742830
1616374089691784263786242128352581128205
1637029808933209990570792006436742620238
9783111470054074998459250360633560933883
8319233867830561364353518921332797329081
3373264265263398976392272340788292817795
3580570993691049175470808931841056146322
3382174656373212482263830921032977016480
5472624384237486241145309381220656491403
2751086643394517512161526545361333111314
0424368548051067658434935238369596534280
7176877532834823434555736671973139274627
3629108210679280784718035329131176778924
6590899386354593278945237776744061922403
3763867400402133034329749690202832814593
3418826817683893072003634795623117103101
2919531697946076327375892535307725523759
4378843450406771555577905645044301664011
9462580972216729758615026968443146952034
6149322911059706762432685159928347098912
8470674086200858713501626031207190317208
6094081298321581077282076353186624611278
2455372085323653057759564300725177443150
5153960090516860322034916322264088524885
2433158051534849622434848299380905070483
4824493274537326245677558790891871908036
6205800959474315005240253270974699531877
0724376825907419939632265984147498193609
2852239450397071654431564213281576889080
5878318340491743455627052022356484649519
6112460268313970975069382648706613264507
6650746115126775227486215986425307112984
4118262266105716351506926002986170494542
5047491378115154139941550671256271197133
2527636319396069028956502882686083622410
8205056243070179497617112123306607331005
9947366875
'''


def large_num_to_s(s):
    return int(''.join([part.strip() for part in s.split('\n')]))


def test_compute_5():
    assert f.compute(5) == FIB_5


def test_compute_100():
    assert f.compute(100) == FIB_100


def test_compute_1000():
    assert f.compute(1000) == int(large_num_to_s(FIB_1000))


def test_compute_10000():
    assert f.compute(10000) == int(large_num_to_s(FIB_10000))


def large_num_to_s(s):
    return int(''.join([part.strip() for part in s.split('\n')]))
