import tempfile

def create_detector() -> str:
    # XML content as a string
    xml_content = """<?xml version="1.0"?>
    <opencv_storage>
    <cascade>
    <stageType>BOOST</stageType>
    <featureType>HAAR</featureType>
    <height>20</height>
    <width>60</width>
    <stageParams>
        <boostType>GAB</boostType>
        <minHitRate>9.9500000476837158e-001</minHitRate>
        <maxFalseAlarm>5.0000000000000000e-001</maxFalseAlarm>
        <weightTrimRate>9.4999999999999996e-001</weightTrimRate>
        <maxDepth>1</maxDepth>
        <maxWeakCount>100</maxWeakCount></stageParams>
    <featureParams>
        <maxCatCount>0</maxCatCount>
        <featSize>1</featSize>
        <mode>ALL</mode></featureParams>
    <stageNum>20</stageNum>
    <stages>
        <!-- stage 0 -->
        <_>
        <maxWeakCount>6</maxWeakCount>
        <stageThreshold>-1.3110191822052002e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 193 1.0079263709485531e-002</internalNodes>
            <leafValues>
                -8.1339186429977417e-001 5.0277775526046753e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 94 -2.2060684859752655e-002</internalNodes>
            <leafValues>
                7.9418992996215820e-001 -5.0896102190017700e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 18 -4.8777908086776733e-002</internalNodes>
            <leafValues>
                7.1656656265258789e-001 -4.1640335321426392e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 35 1.0387318208813667e-002</internalNodes>
            <leafValues>
                3.7618312239646912e-001 -8.5504144430160522e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 191 -9.4083719886839390e-004</internalNodes>
            <leafValues>
                4.2658549547195435e-001 -5.7729166746139526e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 48 -8.2391249015927315e-003</internalNodes>
            <leafValues>
                8.2346975803375244e-001 -3.7503159046173096e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 1 -->
        <_>
        <maxWeakCount>6</maxWeakCount>
        <stageThreshold>-1.1759783029556274e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 21 1.7386786639690399e-001</internalNodes>
            <leafValues>
                -6.8139964342117310e-001 6.0767590999603271e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 28 -1.9797295331954956e-002</internalNodes>
            <leafValues>
                7.8072130680084229e-001 -4.4399836659431458e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 46 -1.0154811898246408e-003</internalNodes>
            <leafValues>
                3.3383268117904663e-001 -7.6357340812683105e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 138 2.4954911321401596e-002</internalNodes>
            <leafValues>
                -3.9979115128517151e-001 6.8620890378952026e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 25 2.8837744612246752e-003</internalNodes>
            <leafValues>
                -2.7928480505943298e-001 7.9980146884918213e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 26 -3.8839362561702728e-002</internalNodes>
            <leafValues>
                -7.8442335128784180e-001 3.4929576516151428e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 2 -->
        <_>
        <maxWeakCount>6</maxWeakCount>
        <stageThreshold>-1.7856997251510620e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 34 2.7977079153060913e-002</internalNodes>
            <leafValues>
                -5.8424139022827148e-001 6.6850829124450684e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 171 1.9148588180541992e-002</internalNodes>
            <leafValues>
                -6.5457659959793091e-001 4.0804430842399597e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 7 1.1955041438341141e-002</internalNodes>
            <leafValues>
                -4.2002618312835693e-001 5.6217432022094727e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 45 -2.1218564361333847e-002</internalNodes>
            <leafValues>
                7.1812576055526733e-001 -3.0354043841362000e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 108 2.0117280655540526e-004</internalNodes>
            <leafValues>
                -6.1749500036239624e-001 3.5549193620681763e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 122 3.9725980604998767e-004</internalNodes>
            <leafValues>
                -2.6844096183776855e-001 7.6771658658981323e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 3 -->
        <_>
        <maxWeakCount>9</maxWeakCount>
        <stageThreshold>-1.1837021112442017e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 202 -1.3291766867041588e-002</internalNodes>
            <leafValues>
                4.5248869061470032e-001 -5.8849954605102539e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 79 -4.8353265970945358e-002</internalNodes>
            <leafValues>
                7.0951640605926514e-001 -3.2546108961105347e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 22 2.6532993651926517e-003</internalNodes>
            <leafValues>
                -2.5343564152717590e-001 7.6588714122772217e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 66 -3.8548894226551056e-002</internalNodes>
            <leafValues>
                5.8126109838485718e-001 -3.0813106894493103e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 41 -6.8602780811488628e-004</internalNodes>
            <leafValues>
                2.6361095905303955e-001 -7.2226840257644653e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 69 -2.5726919993758202e-002</internalNodes>
            <leafValues>
                -8.7153857946395874e-001 1.9438524544239044e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 24 8.4192806389182806e-004</internalNodes>
            <leafValues>
                -3.6150649189949036e-001 5.2065432071685791e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 62 -2.6956878136843443e-003</internalNodes>
            <leafValues>
                5.9945529699325562e-001 -2.8344830870628357e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 112 3.0572075396776199e-002</internalNodes>
            <leafValues>
                -3.0688971281051636e-001 5.7261526584625244e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 4 -->
        <_>
        <maxWeakCount>8</maxWeakCount>
        <stageThreshold>-1.4687808752059937e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 5 3.1486168503761292e-002</internalNodes>
            <leafValues>
                -5.7836848497390747e-001 3.7931033968925476e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 150 2.8311354108154774e-003</internalNodes>
            <leafValues>
                -5.7888329029083252e-001 3.2841828465461731e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 76 -4.2060948908329010e-002</internalNodes>
            <leafValues>
                5.5578106641769409e-001 -3.2662427425384521e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 115 6.2936875037848949e-003</internalNodes>
            <leafValues>
                -2.1032968163490295e-001 7.8646916151046753e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 51 7.0570126175880432e-002</internalNodes>
            <leafValues>
                -4.3683132529258728e-001 4.0298295021057129e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 135 2.5173835456371307e-003</internalNodes>
            <leafValues>
                -2.0461565256118774e-001 8.2858163118362427e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 102 1.5648975968360901e-003</internalNodes>
            <leafValues>
                -2.4848082661628723e-001 6.0209411382675171e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 177 -3.5970686003565788e-003</internalNodes>
            <leafValues>
                2.3294737935066223e-001 -6.5612471103668213e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 5 -->
        <_>
        <maxWeakCount>9</maxWeakCount>
        <stageThreshold>-1.1029583215713501e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 27 -1.1257569491863251e-001</internalNodes>
            <leafValues>
                3.3181819319725037e-001 -5.3901344537734985e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 142 3.8014666642993689e-003</internalNodes>
            <leafValues>
                -3.6430206894874573e-001 4.5984184741973877e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 57 9.8789634648710489e-004</internalNodes>
            <leafValues>
                -2.6661416888237000e-001 5.6971323490142822e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 55 2.1719809621572495e-002</internalNodes>
            <leafValues>
                1.8432702124118805e-001 -8.2999354600906372e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 111 5.1051773130893707e-002</internalNodes>
            <leafValues>
                1.4391148090362549e-001 -9.4541704654693604e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 164 1.8956036074087024e-003</internalNodes>
            <leafValues>
                -6.0830104351043701e-001 2.6091885566711426e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 81 -5.8700828813016415e-003</internalNodes>
            <leafValues>
                6.9104760885238647e-001 -2.6916843652725220e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 116 -1.1522199492901564e-003</internalNodes>
            <leafValues>
                -6.9503885507583618e-001 2.4749211966991425e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 90 -5.1933946087956429e-003</internalNodes>
            <leafValues>
                5.8551025390625000e-001 -3.0389472842216492e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 6 -->
        <_>
        <maxWeakCount>9</maxWeakCount>
        <stageThreshold>-9.0274518728256226e-001</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 205 -1.4383997768163681e-002</internalNodes>
            <leafValues>
                4.5400592684745789e-001 -4.9917897582054138e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 114 -3.3369414508342743e-002</internalNodes>
            <leafValues>
                -9.3247985839843750e-001 1.4586758613586426e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 128 5.2380945999175310e-004</internalNodes>
            <leafValues>
                -2.8349643945693970e-001 6.4983856678009033e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 143 6.1231426661834121e-004</internalNodes>
            <leafValues>
                -1.8502233922481537e-001 6.5052211284637451e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 49 1.7017847858369350e-003</internalNodes>
            <leafValues>
                2.2008989751338959e-001 -7.2277534008026123e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 133 2.6139442343264818e-003</internalNodes>
            <leafValues>
                1.8238025903701782e-001 -7.6262325048446655e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 43 -2.0020073279738426e-003</internalNodes>
            <leafValues>
                5.6799399852752686e-001 -2.8219676017761230e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 119 1.9273828947916627e-003</internalNodes>
            <leafValues>
                -2.0913636684417725e-001 7.9203850030899048e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 134 -9.4476283993571997e-004</internalNodes>
            <leafValues>
                -8.2361942529678345e-001 2.4256958067417145e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 7 -->
        <_>
        <maxWeakCount>10</maxWeakCount>
        <stageThreshold>-1.4518526792526245e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 162 1.6756314784288406e-002</internalNodes>
            <leafValues>
                -6.9359332323074341e-001 5.1373954862356186e-002</leafValues></_>
            <_>
            <internalNodes>
                0 -1 16 2.4082964286208153e-002</internalNodes>
            <leafValues>
                -3.3989402651786804e-001 4.5332714915275574e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 186 1.2284796684980392e-003</internalNodes>
            <leafValues>
                -2.2297365963459015e-001 6.1439812183380127e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 59 -1.4379122294485569e-003</internalNodes>
            <leafValues>
                -6.9444245100021362e-001 2.0446482300758362e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 185 -1.8713285680860281e-003</internalNodes>
            <leafValues>
                6.7942184209823608e-001 -2.7580419182777405e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 190 -4.7389674000442028e-003</internalNodes>
            <leafValues>
                -7.0437240600585938e-001 2.6915156841278076e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 156 7.4071279959753156e-004</internalNodes>
            <leafValues>
                -2.9220902919769287e-001 5.3538239002227783e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 11 -2.2739455103874207e-001</internalNodes>
            <leafValues>
                6.6916191577911377e-001 -2.1987228095531464e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 155 -1.0255509987473488e-003</internalNodes>
            <leafValues>
                6.3346290588378906e-001 -2.2717863321304321e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 167 2.4775355122983456e-003</internalNodes>
            <leafValues>
                -5.4297816753387451e-001 3.1877547502517700e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 8 -->
        <_>
        <maxWeakCount>11</maxWeakCount>
        <stageThreshold>-1.3153649568557739e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 6 1.9131936132907867e-002</internalNodes>
            <leafValues>
                -6.0168600082397461e-001 1.9141913950443268e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 42 -4.5855185016989708e-003</internalNodes>
            <leafValues>
                2.1901632845401764e-001 -5.7136750221252441e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 53 -1.9026801455765963e-003</internalNodes>
            <leafValues>
                -8.0075079202651978e-001 1.6502076387405396e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 19 -3.2767035067081451e-002</internalNodes>
            <leafValues>
                5.1496404409408569e-001 -2.5474679470062256e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 129 6.3941581174731255e-004</internalNodes>
            <leafValues>
                -1.9851709902286530e-001 6.7218667268753052e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 201 1.5573646873235703e-002</internalNodes>
            <leafValues>
                -1.7564551532268524e-001 7.0536541938781738e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 200 9.5508026424795389e-004</internalNodes>
            <leafValues>
                -1.9691802561283112e-001 6.1125624179840088e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 67 9.0427603572607040e-003</internalNodes>
            <leafValues>
                1.6518253087997437e-001 -8.7012130022048950e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 77 8.1576988101005554e-002</internalNodes>
            <leafValues>
                1.4075902104377747e-001 -8.4871828556060791e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 166 -5.1994959358125925e-004</internalNodes>
            <leafValues>
                2.1803210675716400e-001 -5.4628211259841919e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 70 -2.3009868338704109e-002</internalNodes>
            <leafValues>
                -7.9586231708526611e-001 1.5989699959754944e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 9 -->
        <_>
        <maxWeakCount>13</maxWeakCount>
        <stageThreshold>-1.4625015258789063e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 1 2.6759501546621323e-002</internalNodes>
            <leafValues>
                -6.0482984781265259e-001 1.4906832575798035e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 165 3.0343931168317795e-002</internalNodes>
            <leafValues>
                -4.7357541322708130e-001 2.6279065012931824e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 161 1.2678599450737238e-003</internalNodes>
            <leafValues>
                -1.9493983685970306e-001 6.9734728336334229e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 30 1.8607920501381159e-003</internalNodes>
            <leafValues>
                1.5611934661865234e-001 -9.0542370080947876e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 157 -1.3872641138732433e-003</internalNodes>
            <leafValues>
                5.3263407945632935e-001 -3.0192303657531738e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 180 -6.9969398900866508e-003</internalNodes>
            <leafValues>
                -9.4549953937530518e-001 1.5575224161148071e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 158 1.1245720088481903e-003</internalNodes>
            <leafValues>
                -2.6688691973686218e-001 5.5608308315277100e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 160 -2.8279949910938740e-003</internalNodes>
            <leafValues>
                -9.1861122846603394e-001 1.3309663534164429e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 58 7.1019242750480771e-004</internalNodes>
            <leafValues>
                -3.0977895855903625e-001 4.3846300244331360e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 8 -4.1933014988899231e-002</internalNodes>
            <leafValues>
                -8.9102542400360107e-001 1.5866196155548096e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 87 1.6568358987569809e-002</internalNodes>
            <leafValues>
                1.2731756269931793e-001 -8.5553413629531860e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 64 2.0309074316173792e-003</internalNodes>
            <leafValues>
                -2.3260365426540375e-001 6.7330485582351685e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 159 -1.7069760942831635e-003</internalNodes>
            <leafValues>
                -7.1925789117813110e-001 1.9108834862709045e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 10 -->
        <_>
        <maxWeakCount>14</maxWeakCount>
        <stageThreshold>-1.4959813356399536e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 4 1.4695923775434494e-002</internalNodes>
            <leafValues>
                -6.2167906761169434e-001 2.1172638237476349e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 50 -1.6501215286552906e-003</internalNodes>
            <leafValues>
                1.9353884458541870e-001 -5.7780367136001587e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 123 7.0121872704476118e-004</internalNodes>
            <leafValues>
                -2.2979106009006500e-001 5.3033334016799927e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 52 9.4158272258937359e-004</internalNodes>
            <leafValues>
                1.6849038004875183e-001 -7.4897718429565430e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 124 -2.0684124901890755e-003</internalNodes>
            <leafValues>
                6.7936712503433228e-001 -1.9317412376403809e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 23 -1.8305826233699918e-004</internalNodes>
            <leafValues>
                -7.0275229215621948e-001 1.7971208691596985e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 198 5.5587477982044220e-004</internalNodes>
            <leafValues>
                -2.4448128044605255e-001 5.0703984498977661e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 152 4.3448276119306684e-004</internalNodes>
            <leafValues>
                1.3497908413410187e-001 -8.5621362924575806e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 197 -1.2359691318124533e-003</internalNodes>
            <leafValues>
                6.1710417270660400e-001 -2.2301279008388519e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 153 -6.9627340417355299e-004</internalNodes>
            <leafValues>
                -6.4706987142562866e-001 2.3951497673988342e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 175 1.0683680884540081e-003</internalNodes>
            <leafValues>
                -2.8343605995178223e-001 4.9318629503250122e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 168 1.7104238213505596e-004</internalNodes>
            <leafValues>
                -2.7171039581298828e-001 4.2520308494567871e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 144 8.2368971779942513e-003</internalNodes>
            <leafValues>
                1.6359315812587738e-001 -7.3864609003067017e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 131 -5.9884190559387207e-003</internalNodes>
            <leafValues>
                3.8030940294265747e-001 -3.0763563513755798e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 11 -->
        <_>
        <maxWeakCount>9</maxWeakCount>
        <stageThreshold>-1.1183819770812988e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 187 -1.4863962307572365e-002</internalNodes>
            <leafValues>
                1.1989101022481918e-001 -6.6138857603073120e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 117 2.4736612103879452e-003</internalNodes>
            <leafValues>
                -5.2778661251068115e-001 2.3012125492095947e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 71 -4.8899287357926369e-003</internalNodes>
            <leafValues>
                6.0186779499053955e-001 -2.0681641995906830e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 174 1.5796069055795670e-002</internalNodes>
            <leafValues>
                1.4610521495342255e-001 -8.2099527120590210e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 104 5.9720675926655531e-004</internalNodes>
            <leafValues>
                -2.3587301373481750e-001 4.8323699831962585e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 103 -1.9448818638920784e-003</internalNodes>
            <leafValues>
                6.4417767524719238e-001 -2.0953170955181122e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 154 1.9433414854574949e-004</internalNodes>
            <leafValues>
                2.0600238442420959e-001 -7.2418999671936035e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 163 -1.5097535215318203e-002</internalNodes>
            <leafValues>
                -8.7151485681533813e-001 1.2594890594482422e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 82 -3.9843879640102386e-003</internalNodes>
            <leafValues>
                4.3801131844520569e-001 -2.9676589369773865e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 12 -->
        <_>
        <maxWeakCount>12</maxWeakCount>
        <stageThreshold>-1.5434337854385376e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 105 1.1273270938545465e-003</internalNodes>
            <leafValues>
                -4.7976878285408020e-001 3.6627906560897827e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 95 9.7806821577250957e-004</internalNodes>
            <leafValues>
                -2.7689707279205322e-001 5.1295894384384155e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 15 1.6528377309441566e-002</internalNodes>
            <leafValues>
                -4.5259797573089600e-001 2.4290211498737335e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 137 1.1040373938158154e-003</internalNodes>
            <leafValues>
                -3.2714816927909851e-001 3.4566244482994080e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 109 -1.7780361231416464e-003</internalNodes>
            <leafValues>
                -6.9511681795120239e-001 1.8829824030399323e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 92 4.6280334936454892e-004</internalNodes>
            <leafValues>
                -2.3864887654781342e-001 5.3136289119720459e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 100 -1.4975425438024104e-004</internalNodes>
            <leafValues>
                -6.6509884595870972e-001 2.1483559906482697e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 83 -1.4625370968133211e-003</internalNodes>
            <leafValues>
                2.6556470990180969e-001 -4.9002227187156677e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 14 -2.6019819779321551e-004</internalNodes>
            <leafValues>
                -7.0160359144210815e-001 1.6359129548072815e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 14 2.2371641534846276e-004</internalNodes>
            <leafValues>
                1.2919521331787109e-001 -6.9767206907272339e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 194 -1.0447315871715546e-002</internalNodes>
            <leafValues>
                2.1837629377841949e-001 -4.6482038497924805e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 20 -9.2897024005651474e-003</internalNodes>
            <leafValues>
                6.4918082952499390e-001 -2.0495061576366425e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 13 -->
        <_>
        <maxWeakCount>12</maxWeakCount>
        <stageThreshold>-1.4440233707427979e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 9 8.5356216877698898e-003</internalNodes>
            <leafValues>
                -5.3151458501815796e-001 2.2357723116874695e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 182 1.5294685726985335e-003</internalNodes>
            <leafValues>
                -6.0895460844039917e-001 1.7429886758327484e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 40 1.8610086990520358e-003</internalNodes>
            <leafValues>
                -2.5480428338050842e-001 4.2150071263313293e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 176 1.5735558699816465e-003</internalNodes>
            <leafValues>
                -1.6832062602043152e-001 4.8567819595336914e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 179 -6.7992787808179855e-004</internalNodes>
            <leafValues>
                3.9894598722457886e-001 -3.0744269490242004e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 151 4.9857296049594879e-002</internalNodes>
            <leafValues>
                -1.5370152890682220e-001 6.7523348331451416e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 139 -2.8339058160781860e-002</internalNodes>
            <leafValues>
                5.0540882349014282e-001 -2.9473617672920227e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 72 -7.7956825494766235e-002</internalNodes>
            <leafValues>
                4.0387043356895447e-001 -3.0287107825279236e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 89 -3.6115488037467003e-003</internalNodes>
            <leafValues>
                6.3856112957000732e-001 -1.6917882859706879e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 207 3.3940275898203254e-004</internalNodes>
            <leafValues>
                1.3713537156581879e-001 -7.8120291233062744e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 39 4.0043061599135399e-003</internalNodes>
            <leafValues>
                1.5233094990253448e-001 -6.3939732313156128e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 65 -4.4601649278774858e-004</internalNodes>
            <leafValues>
                2.1333815157413483e-001 -4.7728902101516724e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 14 -->
        <_>
        <maxWeakCount>13</maxWeakCount>
        <stageThreshold>-1.2532578706741333e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 204 -2.0341124385595322e-002</internalNodes>
            <leafValues>
                2.4170616269111633e-001 -4.9161517620086670e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 169 8.9040049351751804e-004</internalNodes>
            <leafValues>
                -2.8570893406867981e-001 4.2666998505592346e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 60 -3.3259526826441288e-003</internalNodes>
            <leafValues>
                4.2626520991325378e-001 -2.3811897635459900e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 38 -3.1714607030153275e-002</internalNodes>
            <leafValues>
                -8.5494768619537354e-001 1.1712870001792908e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 31 -1.1553820222616196e-002</internalNodes>
            <leafValues>
                2.2675493359565735e-001 -4.9640509486198425e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 80 -6.7727260291576385e-002</internalNodes>
            <leafValues>
                -8.6705064773559570e-001 9.8765812814235687e-002</leafValues></_>
            <_>
            <internalNodes>
                0 -1 63 -3.1611192971467972e-003</internalNodes>
            <leafValues>
                3.9449846744537354e-001 -2.8210711479187012e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 149 4.3221906526014209e-004</internalNodes>
            <leafValues>
                1.1805476248264313e-001 -9.0178310871124268e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 188 -2.2296360111795366e-004</internalNodes>
            <leafValues>
                1.7324598133563995e-001 -5.2877873182296753e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 120 -2.1440195851027966e-003</internalNodes>
            <leafValues>
                5.5513423681259155e-001 -1.9791823625564575e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 113 -4.5122690498828888e-003</internalNodes>
            <leafValues>
                5.5083745718002319e-001 -1.8810540437698364e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 130 -3.5149464383721352e-003</internalNodes>
            <leafValues>
                5.5467557907104492e-001 -2.2856147587299347e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 121 -4.4786706566810608e-003</internalNodes>
            <leafValues>
                -7.9106998443603516e-001 1.7836479842662811e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 15 -->
        <_>
        <maxWeakCount>15</maxWeakCount>
        <stageThreshold>-1.1898330450057983e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 0 1.5206767246127129e-002</internalNodes>
            <leafValues>
                -4.9173194169998169e-001 2.7093595266342163e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 125 6.9564773002639413e-004</internalNodes>
            <leafValues>
                -2.3066598176956177e-001 5.4028344154357910e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 125 -8.3668017759919167e-004</internalNodes>
            <leafValues>
                4.4658055901527405e-001 -2.7778497338294983e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 91 -3.8321319967508316e-002</internalNodes>
            <leafValues>
                -7.9069298505783081e-001 1.8700349330902100e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 207 -2.1063965687062591e-004</internalNodes>
            <leafValues>
                -6.3163763284683228e-001 1.8656146526336670e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 61 3.6907330155372620e-002</internalNodes>
            <leafValues>
                9.9319733679294586e-002 -7.6762360334396362e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 85 8.1071127206087112e-003</internalNodes>
            <leafValues>
                -2.8561261296272278e-001 3.4748569130897522e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 189 6.2815943965688348e-004</internalNodes>
            <leafValues>
                1.6656193137168884e-001 -5.4635977745056152e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 86 2.8582263621501625e-004</internalNodes>
            <leafValues>
                -2.4100163578987122e-001 4.5410770177841187e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 173 -1.9862279295921326e-002</internalNodes>
            <leafValues>
                -9.4317340850830078e-001 1.2513674795627594e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 96 1.1506280861794949e-003</internalNodes>
            <leafValues>
                -2.4514634907245636e-001 4.6452957391738892e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 29 2.3451185552403331e-004</internalNodes>
            <leafValues>
                1.2489952147006989e-001 -8.0278074741363525e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 101 6.7837134702131152e-004</internalNodes>
            <leafValues>
                -2.5017899274826050e-001 4.3841627240180969e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 17 3.1583159579895437e-004</internalNodes>
            <leafValues>
                1.5951988101005554e-001 -7.4524724483489990e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 110 7.2623658925294876e-003</internalNodes>
            <leafValues>
                1.2511830031871796e-001 -6.5659755468368530e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 16 -->
        <_>
        <maxWeakCount>15</maxWeakCount>
        <stageThreshold>-1.2416906356811523e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 2 7.5144092552363873e-003</internalNodes>
            <leafValues>
                -5.9518074989318848e-001 5.3793102502822876e-002</leafValues></_>
            <_>
            <internalNodes>
                0 -1 98 -6.4494344405829906e-004</internalNodes>
            <leafValues>
                2.0429474115371704e-001 -4.3661779165267944e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 196 3.3831471228040755e-004</internalNodes>
            <leafValues>
                -2.1566553413867950e-001 4.7118204832077026e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 73 2.8320802375674248e-003</internalNodes>
            <leafValues>
                1.3322307169437408e-001 -8.3729231357574463e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 199 1.6218879027292132e-003</internalNodes>
            <leafValues>
                -2.0889574289321899e-001 4.7114694118499756e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 10 2.7122153551317751e-004</internalNodes>
            <leafValues>
                1.1475630849599838e-001 -7.8029519319534302e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 170 8.8358242064714432e-003</internalNodes>
            <leafValues>
                1.2460929155349731e-001 -7.6791721582412720e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 106 9.7634072881191969e-004</internalNodes>
            <leafValues>
                -2.0806105434894562e-001 5.1318311691284180e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 107 -2.1239042282104492e-002</internalNodes>
            <leafValues>
                -8.7171542644500732e-001 1.2721680104732513e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 97 7.1797124110162258e-004</internalNodes>
            <leafValues>
                -3.0763280391693115e-001 3.7504923343658447e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 32 2.7504155412316322e-002</internalNodes>
            <leafValues>
                1.5651945769786835e-001 -7.9516488313674927e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 178 1.0624636197462678e-003</internalNodes>
            <leafValues>
                1.3473348319530487e-001 -6.9174814224243164e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 33 -8.1248432397842407e-002</internalNodes>
            <leafValues>
                -8.5117286443710327e-001 1.0601779073476791e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 140 -2.2936165332794189e-002</internalNodes>
            <leafValues>
                3.9202499389648438e-001 -2.9867398738861084e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 146 -1.3326616026461124e-003</internalNodes>
            <leafValues>
                4.7240665555000305e-001 -2.6287403702735901e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 17 -->
        <_>
        <maxWeakCount>13</maxWeakCount>
        <stageThreshold>-1.3383979797363281e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 3 3.2254494726657867e-002</internalNodes>
            <leafValues>
                -6.5151512622833252e-001 7.9947575926780701e-002</leafValues></_>
            <_>
            <internalNodes>
                0 -1 172 -1.1810796568170190e-003</internalNodes>
            <leafValues>
                2.5173431634902954e-001 -4.5536977052688599e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 88 8.0361258005723357e-004</internalNodes>
            <leafValues>
                -2.1178695559501648e-001 4.9318632483482361e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 93 6.6201295703649521e-004</internalNodes>
            <leafValues>
                -1.9441033899784088e-001 4.6225026249885559e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 84 3.4565184614621103e-004</internalNodes>
            <leafValues>
                -2.1175089478492737e-001 4.6985754370689392e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 132 -5.6433549616485834e-004</internalNodes>
            <leafValues>
                -7.9713624715805054e-001 1.8714086711406708e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 56 5.8492692187428474e-004</internalNodes>
            <leafValues>
                -3.9330720901489258e-001 2.4242231249809265e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 13 2.5043603032827377e-002</internalNodes>
            <leafValues>
                1.3490234315395355e-001 -7.5923883914947510e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 37 -1.8510785885155201e-003</internalNodes>
            <leafValues>
                4.1279399394989014e-001 -2.7271771430969238e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 68 -2.5741360150277615e-004</internalNodes>
            <leafValues>
                -6.3662034273147583e-001 1.8135882914066315e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 184 -1.5121832489967346e-002</internalNodes>
            <leafValues>
                2.5249326229095459e-001 -3.8438034057617188e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 203 -1.5006031841039658e-002</internalNodes>
            <leafValues>
                -8.4878319501876831e-001 1.1718367785215378e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 74 4.9880752339959145e-004</internalNodes>
            <leafValues>
                -2.6755046844482422e-001 4.5769825577735901e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 18 -->
        <_>
        <maxWeakCount>12</maxWeakCount>
        <stageThreshold>-1.2097512483596802e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 195 -1.1614991351962090e-002</internalNodes>
            <leafValues>
                1.4465409517288208e-001 -5.9521216154098511e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 75 3.9767110138200223e-004</internalNodes>
            <leafValues>
                -4.2697989940643311e-001 2.4382311105728149e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 47 -4.6969857066869736e-002</internalNodes>
            <leafValues>
                -9.3969690799713135e-001 1.2196484953165054e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 136 5.5550434626638889e-004</internalNodes>
            <leafValues>
                -1.8246935307979584e-001 6.5156191587448120e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 99 2.9468833236023784e-004</internalNodes>
            <leafValues>
                1.5099152922630310e-001 -7.8840750455856323e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 44 1.2439775280654430e-002</internalNodes>
            <leafValues>
                1.4981375634670258e-001 -7.5917595624923706e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 147 6.6337559837847948e-004</internalNodes>
            <leafValues>
                -2.5185841321945190e-001 5.9387433528900146e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 148 -6.8454549182206392e-004</internalNodes>
            <leafValues>
                5.1199448108673096e-001 -2.5247576832771301e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 141 1.4808592386543751e-003</internalNodes>
            <leafValues>
                2.2439701855182648e-001 -5.8184891939163208e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 12 6.0307271778583527e-003</internalNodes>
            <leafValues>
                -4.3553912639617920e-001 2.8183382749557495e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 78 -1.9170897081494331e-002</internalNodes>
            <leafValues>
                -8.5707378387451172e-001 1.4850790798664093e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 122 3.0278289341367781e-004</internalNodes>
            <leafValues>
                -3.1547480821609497e-001 4.1798374056816101e-001</leafValues></_></weakClassifiers></_>
        <!-- stage 19 -->
        <_>
        <maxWeakCount>10</maxWeakCount>
        <stageThreshold>-1.2253109216690063e+000</stageThreshold>
        <weakClassifiers>
            <_>
            <internalNodes>
                0 -1 181 4.6847470104694366e-002</internalNodes>
            <leafValues>
                -4.9239391088485718e-001 5.2287584543228149e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 118 2.2181579843163490e-003</internalNodes>
            <leafValues>
                -4.2569425702095032e-001 3.6892616748809814e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 145 6.1082182219251990e-004</internalNodes>
            <leafValues>
                1.7654621601104736e-001 -8.2656937837600708e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 127 1.7401995137333870e-002</internalNodes>
            <leafValues>
                2.7770876884460449e-001 -5.6393522024154663e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 54 5.2314018830657005e-004</internalNodes>
            <leafValues>
                -3.6257097125053406e-001 4.6126455068588257e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 206 2.1581796463578939e-003</internalNodes>
            <leafValues>
                1.9110183417797089e-001 -6.8012320995330811e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 192 -1.3209994649514556e-003</internalNodes>
            <leafValues>
                6.7618584632873535e-001 -2.6087108254432678e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 126 -1.2237254530191422e-002</internalNodes>
            <leafValues>
                -5.7184767723083496e-001 3.0778104066848755e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 36 8.7829465046525002e-003</internalNodes>
            <leafValues>
                1.6890920698642731e-001 -7.8835797309875488e-001</leafValues></_>
            <_>
            <internalNodes>
                0 -1 183 7.5588272884488106e-003</internalNodes>
            <leafValues>
                1.5143942832946777e-001 -8.2572847604751587e-001</leafValues></_></weakClassifiers></_></stages>
    <features>
        <_>
        <rects>
            <_>
            0 0 10 10 -1.</_>
            <_>
            0 0 5 5 2.</_>
            <_>
            5 5 5 5 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            0 0 12 16 -1.</_>
            <_>
            6 0 6 16 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            0 3 10 6 -1.</_>
            <_>
            5 3 5 6 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            0 3 21 16 -1.</_>
            <_>
            7 3 7 16 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            0 4 16 9 -1.</_>
            <_>
            4 4 8 9 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            0 4 10 12 -1.</_>
            <_>
            5 4 5 12 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            0 7 14 7 -1.</_>
            <_>
            7 7 7 7 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            0 9 12 7 -1.</_>
            <_>
            6 9 6 7 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            0 9 60 3 -1.</_>
            <_>
            30 9 30 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            0 10 8 3 -1.</_>
            <_>
            4 10 4 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            0 11 1 2 -1.</_>
            <_>
            0 12 1 1 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            1 0 51 12 -1.</_>
            <_>
            1 4 51 4 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            1 3 15 7 -1.</_>
            <_>
            6 3 5 7 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            1 7 30 6 -1.</_>
            <_>
            1 7 15 3 2.</_>
            <_>
            16 10 15 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            1 12 1 2 -1.</_>
            <_>
            1 13 1 1 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            2 2 18 16 -1.</_>
            <_>
            2 6 18 8 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            2 3 29 4 -1.</_>
            <_>
            2 5 29 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            2 9 1 2 -1.</_>
            <_>
            2 10 1 1 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            2 14 40 6 -1.</_>
            <_>
            2 17 40 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            3 0 22 6 -1.</_>
            <_>
            3 2 22 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            3 2 38 2 -1.</_>
            <_>
            3 2 19 1 2.</_>
            <_>
            22 3 19 1 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            3 4 51 16 -1.</_>
            <_>
            3 8 51 8 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            3 7 3 8 -1.</_>
            <_>
            4 7 1 8 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            3 9 1 3 -1.</_>
            <_>
            3 10 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            4 8 3 5 -1.</_>
            <_>
            5 8 1 5 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            4 8 4 9 -1.</_>
            <_>
            5 8 2 9 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            4 11 36 9 -1.</_>
            <_>
            16 11 12 9 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            4 14 49 6 -1.</_>
            <_>
            4 17 49 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            5 0 17 6 -1.</_>
            <_>
            5 2 17 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            5 1 3 1 -1.</_>
            <_>
            6 1 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            5 1 8 2 -1.</_>
            <_>
            7 1 4 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            5 2 36 9 -1.</_>
            <_>
            17 2 12 9 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            5 3 33 17 -1.</_>
            <_>
            16 3 11 17 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            6 0 30 19 -1.</_>
            <_>
            16 0 10 19 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            6 3 29 4 -1.</_>
            <_>
            6 5 29 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            6 4 16 16 -1.</_>
            <_>
            14 4 8 16 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            6 9 54 1 -1.</_>
            <_>
            33 9 27 1 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            7 0 4 18 -1.</_>
            <_>
            8 0 2 18 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            7 3 12 15 -1.</_>
            <_>
            13 3 6 15 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            7 4 20 5 -1.</_>
            <_>
            12 4 10 5 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            7 4 6 3 -1.</_>
            <_>
            7 5 6 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            7 4 36 6 -1.</_>
            <_>
            19 4 12 6 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            7 5 28 4 -1.</_>
            <_>
            14 5 14 4 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            7 7 4 11 -1.</_>
            <_>
            8 7 2 11 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            7 9 12 7 -1.</_>
            <_>
            13 9 6 7 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            8 1 21 4 -1.</_>
            <_>
            8 3 21 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            8 4 28 6 -1.</_>
            <_>
            15 4 14 6 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            8 8 38 6 -1.</_>
            <_>
            8 10 38 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            8 14 25 4 -1.</_>
            <_>
            8 15 25 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            9 2 12 4 -1.</_>
            <_>
            12 2 6 4 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            9 5 24 3 -1.</_>
            <_>
            15 5 12 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            9 8 40 12 -1.</_>
            <_>
            9 12 40 4 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            10 2 8 2 -1.</_>
            <_>
            12 2 4 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            10 2 9 2 -1.</_>
            <_>
            13 2 3 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            10 5 3 3 -1.</_>
            <_>
            11 6 1 1 9.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            11 0 32 20 -1.</_>
            <_>
            19 0 16 20 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            11 3 1 4 -1.</_>
            <_>
            11 5 1 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            11 9 4 3 -1.</_>
            <_>
            12 9 2 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            11 9 3 7 -1.</_>
            <_>
            12 9 1 7 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            12 3 9 2 -1.</_>
            <_>
            15 3 3 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            12 6 6 6 -1.</_>
            <_>
            14 6 2 6 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            12 10 42 10 -1.</_>
            <_>
            26 10 14 10 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            12 14 11 3 -1.</_>
            <_>
            12 15 11 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            13 4 6 14 -1.</_>
            <_>
            15 4 2 14 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            13 8 3 6 -1.</_>
            <_>
            14 8 1 6 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            13 11 32 2 -1.</_>
            <_>
            21 11 16 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            13 13 25 6 -1.</_>
            <_>
            13 16 25 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            13 16 21 3 -1.</_>
            <_>
            20 16 7 3 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            14 2 3 2 -1.</_>
            <_>
            15 2 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            14 2 24 8 -1.</_>
            <_>
            20 2 12 8 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            14 13 36 6 -1.</_>
            <_>
            23 13 18 6 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            14 14 8 3 -1.</_>
            <_>
            14 15 8 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            14 14 45 6 -1.</_>
            <_>
            14 17 45 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            14 18 9 2 -1.</_>
            <_>
            17 18 3 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            15 9 4 1 -1.</_>
            <_>
            16 9 2 1 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            15 10 19 4 -1.</_>
            <_>
            15 12 19 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            16 0 28 8 -1.</_>
            <_>
            16 2 28 4 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            16 2 36 18 -1.</_>
            <_>
            28 2 12 18 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            16 6 24 6 -1.</_>
            <_>
            22 6 12 6 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            17 1 24 6 -1.</_>
            <_>
            17 3 24 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            17 3 15 12 -1.</_>
            <_>
            22 7 5 4 9.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            17 15 11 3 -1.</_>
            <_>
            17 16 11 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            18 5 6 10 -1.</_>
            <_>
            20 5 2 10 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            18 6 18 3 -1.</_>
            <_>
            24 6 6 3 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            18 11 3 1 -1.</_>
            <_>
            19 11 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            19 6 32 2 -1.</_>
            <_>
            27 6 16 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            19 8 3 1 -1.</_>
            <_>
            20 8 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            19 9 14 11 -1.</_>
            <_>
            26 9 7 11 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            19 10 3 3 -1.</_>
            <_>
            20 10 1 3 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            19 13 7 3 -1.</_>
            <_>
            19 14 7 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            19 14 13 3 -1.</_>
            <_>
            19 15 13 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            20 0 15 20 -1.</_>
            <_>
            25 0 5 20 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            20 9 3 1 -1.</_>
            <_>
            21 9 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            20 10 3 2 -1.</_>
            <_>
            21 10 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            21 1 21 6 -1.</_>
            <_>
            21 3 21 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            21 8 4 3 -1.</_>
            <_>
            22 8 2 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            21 9 3 4 -1.</_>
            <_>
            22 9 1 4 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            21 10 4 2 -1.</_>
            <_>
            22 10 2 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            21 11 24 2 -1.</_>
            <_>
            27 11 12 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            21 18 4 1 -1.</_>
            <_>
            22 18 2 1 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            22 3 4 1 -1.</_>
            <_>
            23 3 2 1 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            22 6 2 6 -1.</_>
            <_>
            22 6 1 3 2.</_>
            <_>
            23 9 1 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            22 7 3 3 -1.</_>
            <_>
            23 8 1 1 9.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            22 8 3 5 -1.</_>
            <_>
            23 8 1 5 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            22 9 3 2 -1.</_>
            <_>
            23 9 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            23 8 3 3 -1.</_>
            <_>
            24 8 1 3 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            23 10 3 2 -1.</_>
            <_>
            24 10 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            24 3 20 17 -1.</_>
            <_>
            29 3 10 17 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            24 4 14 6 -1.</_>
            <_>
            31 4 7 6 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            24 18 9 2 -1.</_>
            <_>
            27 18 3 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            25 5 8 4 -1.</_>
            <_>
            25 5 4 4 2.</_></rects>
        <tilted>1</tilted></_>
        <_>
        <rects>
            <_>
            25 6 22 14 -1.</_>
            <_>
            36 6 11 14 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            25 12 28 8 -1.</_>
            <_>
            25 14 28 4 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            25 14 9 3 -1.</_>
            <_>
            25 15 9 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            26 2 27 18 -1.</_>
            <_>
            35 2 9 18 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            26 3 22 3 -1.</_>
            <_>
            26 4 22 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            26 4 8 4 -1.</_>
            <_>
            30 4 4 4 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            26 4 20 6 -1.</_>
            <_>
            31 4 10 6 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            26 7 1 12 -1.</_>
            <_>
            22 11 1 4 3.</_></rects>
        <tilted>1</tilted></_>
        <_>
        <rects>
            <_>
            26 9 3 3 -1.</_>
            <_>
            27 9 1 3 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            26 13 9 3 -1.</_>
            <_>
            26 14 9 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            27 3 15 6 -1.</_>
            <_>
            32 3 5 6 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            27 9 3 1 -1.</_>
            <_>
            28 9 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            27 9 3 2 -1.</_>
            <_>
            28 9 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            27 10 3 3 -1.</_>
            <_>
            28 10 1 3 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            27 11 3 2 -1.</_>
            <_>
            28 11 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            28 2 10 4 -1.</_>
            <_>
            28 2 10 2 2.</_></rects>
        <tilted>1</tilted></_>
        <_>
        <rects>
            <_>
            28 8 32 6 -1.</_>
            <_>
            28 10 32 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            28 10 3 1 -1.</_>
            <_>
            29 10 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            28 11 3 1 -1.</_>
            <_>
            29 11 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            28 15 5 4 -1.</_>
            <_>
            28 16 5 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            28 16 23 4 -1.</_>
            <_>
            28 17 23 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            28 19 6 1 -1.</_>
            <_>
            30 19 2 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            29 3 9 4 -1.</_>
            <_>
            32 3 3 4 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            29 5 9 1 -1.</_>
            <_>
            32 5 3 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            29 8 3 6 -1.</_>
            <_>
            30 8 1 6 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            29 9 3 1 -1.</_>
            <_>
            30 9 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            29 11 10 4 -1.</_>
            <_>
            29 13 10 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            29 11 26 8 -1.</_>
            <_>
            29 13 26 4 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            30 0 16 6 -1.</_>
            <_>
            30 3 16 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            30 2 30 6 -1.</_>
            <_>
            30 2 15 3 2.</_>
            <_>
            45 5 15 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            30 3 9 4 -1.</_>
            <_>
            33 3 3 4 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            30 5 9 4 -1.</_>
            <_>
            30 6 9 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            30 10 3 2 -1.</_>
            <_>
            31 10 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            30 14 18 6 -1.</_>
            <_>
            36 14 6 6 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            31 3 4 3 -1.</_>
            <_>
            32 3 2 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            31 7 4 9 -1.</_>
            <_>
            32 7 2 9 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            31 11 3 2 -1.</_>
            <_>
            32 11 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            31 11 3 3 -1.</_>
            <_>
            32 11 1 3 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            32 4 3 2 -1.</_>
            <_>
            33 4 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            32 6 18 6 -1.</_>
            <_>
            32 6 9 3 2.</_>
            <_>
            41 9 9 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            33 1 22 6 -1.</_>
            <_>
            33 4 22 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            33 3 4 2 -1.</_>
            <_>
            34 3 2 2 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            33 3 4 4 -1.</_>
            <_>
            34 3 2 4 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            33 5 4 1 -1.</_>
            <_>
            34 5 2 1 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            33 9 3 6 -1.</_>
            <_>
            34 9 1 6 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            33 10 3 3 -1.</_>
            <_>
            34 10 1 3 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            34 8 4 7 -1.</_>
            <_>
            35 8 2 7 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            34 9 3 5 -1.</_>
            <_>
            35 9 1 5 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            34 18 9 2 -1.</_>
            <_>
            37 18 3 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            35 0 8 6 -1.</_>
            <_>
            37 0 4 6 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            35 9 3 2 -1.</_>
            <_>
            36 9 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            36 9 24 9 -1.</_>
            <_>
            42 9 12 9 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            37 1 16 18 -1.</_>
            <_>
            41 1 8 18 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            37 11 20 8 -1.</_>
            <_>
            42 11 10 8 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            38 8 15 12 -1.</_>
            <_>
            38 12 15 4 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            39 6 12 8 -1.</_>
            <_>
            45 6 6 8 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            40 8 8 4 -1.</_>
            <_>
            40 8 8 2 2.</_></rects>
        <tilted>1</tilted></_>
        <_>
        <rects>
            <_>
            40 10 3 1 -1.</_>
            <_>
            41 10 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            40 10 3 5 -1.</_>
            <_>
            41 10 1 5 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            40 13 12 6 -1.</_>
            <_>
            43 13 6 6 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            41 5 7 15 -1.</_>
            <_>
            41 10 7 5 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            41 6 12 6 -1.</_>
            <_>
            45 6 4 6 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            41 7 12 7 -1.</_>
            <_>
            45 7 4 7 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            41 8 12 12 -1.</_>
            <_>
            45 8 4 12 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            41 9 3 6 -1.</_>
            <_>
            42 9 1 6 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            42 2 3 13 -1.</_>
            <_>
            43 2 1 13 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            42 4 18 10 -1.</_>
            <_>
            42 4 9 5 2.</_>
            <_>
            51 9 9 5 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            42 5 18 8 -1.</_>
            <_>
            42 5 9 4 2.</_>
            <_>
            51 9 9 4 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            42 7 2 7 -1.</_>
            <_>
            43 7 1 7 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            42 14 12 5 -1.</_>
            <_>
            46 14 4 5 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            43 1 10 9 -1.</_>
            <_>
            40 4 10 3 3.</_></rects>
        <tilted>1</tilted></_>
        <_>
        <rects>
            <_>
            43 6 6 6 -1.</_>
            <_>
            43 9 6 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            44 0 8 20 -1.</_>
            <_>
            46 0 4 20 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            44 2 16 12 -1.</_>
            <_>
            44 2 8 6 2.</_>
            <_>
            52 8 8 6 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            44 5 3 8 -1.</_>
            <_>
            45 5 1 8 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            44 8 3 4 -1.</_>
            <_>
            45 8 1 4 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            44 12 16 4 -1.</_>
            <_>
            52 12 8 4 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            44 13 10 3 -1.</_>
            <_>
            49 13 5 3 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            45 19 9 1 -1.</_>
            <_>
            48 19 3 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            46 3 8 8 -1.</_>
            <_>
            50 3 4 8 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            47 12 10 6 -1.</_>
            <_>
            52 12 5 6 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            48 0 4 13 -1.</_>
            <_>
            49 0 2 13 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            48 5 3 12 -1.</_>
            <_>
            45 8 3 6 2.</_></rects>
        <tilted>1</tilted></_>
        <_>
        <rects>
            <_>
            48 9 12 8 -1.</_>
            <_>
            54 9 6 8 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            48 13 12 4 -1.</_>
            <_>
            54 13 6 4 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            49 8 3 1 -1.</_>
            <_>
            50 8 1 1 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            49 8 3 2 -1.</_>
            <_>
            50 8 1 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            49 8 3 3 -1.</_>
            <_>
            50 8 1 3 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            50 9 3 3 -1.</_>
            <_>
            51 10 1 1 9.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            51 8 3 3 -1.</_>
            <_>
            52 8 1 3 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            52 6 6 10 -1.</_>
            <_>
            54 6 2 10 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            52 7 8 7 -1.</_>
            <_>
            56 7 4 7 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            52 8 8 4 -1.</_>
            <_>
            52 8 8 2 2.</_></rects>
        <tilted>1</tilted></_>
        <_>
        <rects>
            <_>
            54 3 6 15 -1.</_>
            <_>
            57 3 3 15 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            54 8 6 7 -1.</_>
            <_>
            57 8 3 7 2.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            57 11 3 6 -1.</_>
            <_>
            57 13 3 2 3.</_></rects>
        <tilted>0</tilted></_>
        <_>
        <rects>
            <_>
            59 8 1 3 -1.</_>
            <_>
            59 9 1 1 3.</_></rects>
        <tilted>0</tilted></_></features></cascade>
    </opencv_storage>"""

    # Create a temporary file and write the XML content to it
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xml') as temp:
        temp.write(xml_content.encode('utf-8'))
        temp_path = temp.name
    
    return temp_path