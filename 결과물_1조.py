gra={}
gra['교양(기초)'] = '기초교양 13학점 이수'
gra1={}
gra1['교양(상명핵심역량)'] = '상명핵심역량교양 4학점 이상 이수'
gra2={}
gra2['교양(균형)'] = '균형교양 9학점 이상 이수'
gra3={}
gra3['교양(총괄)']= '일반교양 포함 전체 교양 총 33학점 이상 이수'

gra4={}
gra4['전공학점(심화전공)'] = '총 60학점 이상, 전공심화 15학점 이상 포함'
gra5={}
gra5['전공학점(다전공)'] = '각 전공 36학점 이상'
gra6={}
gra6['전공학점(부전공)'] = '주전공 60학점 이상, 부전공 21학점 이상'
gra7={}
gra7['졸업고사(자격)']= '4학년 2학기(이수학기 8학기 이상) 재학 중인 재학생 및 수료자, 행정통계학 수강, 졸업고사 관련 7과목 중 5과목 이상 수강완료'
gra8={}
gra8['졸업고사(통과기준)']='<인적자원관리론 = 인사행정>, <e-거버먼트와 정보보호 = 전자정부>, <전략기획론 = 전략기획과 혁신 = 미래예측과 기획>, <공공관리론>, <재무행정론 = 공공재무회계론>, <조직행태론>, <헌법 1 = 국가와 기본권(행정학과 X)>, 7과목 평균 60점 이상'
print("")

print("!!!!!!!상명대 행정학부 졸업안내!!!!!!!!")
print("대답 -> !! 반드시o/x !!")

ans0=input("프로젝트 시작 전 졸업요건에 대한 간략한 설명을 해드릴까요? : ")

if ans0== 'o':
    print(gra)
    print()
    print(gra1)
    print()
    print(gra2)
    print()
    print(gra3)
    print()
    print(gra4)
    print()
    print(gra5)
    print()
    print(gra6)
    print()
    print(gra7)
    print()
    print(gra8)
    print()
    ans1=input("상명대학교 행정학부 졸업프로젝트를 시작할까요? : ")
    print()

    if ans1== 'o' :
        print()
        print()
        print()
        print("<교양 관련 질문 START>")
        print()
        ans2=input("기초교양(13학점)을 모두 이수하였는가? : ")
        print()
        if ans2=='o' :
            ans3=input("상명핵심역량교양(4학점 이상)을 모두 이수하였는가? : ")
            print()
            if ans3== 'o' :
                ans4=input("균형교양(9학점 이상)을 모두 이수하였는가? : ")
                print()
                if ans4== 'o':
                    ans5=input("일반교양 포함 전체 교양 총 33학점 이상을 이수하였는가? : ")
                    print()
                    if ans5== 'o':
                        print("***교양 관련 졸업 조건 모두 충족***")
                        print()
                        print()
                        print()
                        print("<전공 관련 질문 START>")
                        ans6=input("심화전공, 다전공, 부전공 중 하나의 조건에서 전공 학점을 모두 이수하였는가? : ")
                        print()
                        if ans6=='o':
                            ans7=input("졸업고사 자격을 충족하였는가? : ")
                            print()
                            if ans7=='o':
                                ans8=input("졸업고사에 응시하여 통과하였는가? : ")
                                print()
                                if ans8=='o':
                                    print("♥축하합니다. 졸업이 가능합니다♥")

                                elif ans8=='x':
                                    print("※ 아쉽지만 졸업고사에 통과해야합니다 ※")

                                else:
                                    print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

                            elif ans7=='x':
                                print("◆8학기 이상을 이수하고 졸업시험 7과목 중 5과목과 행정통계학을 수강해야 합니다◆")

                            else :
                                print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

                        elif ans6=='x':
                            print("◆전공 학점 추가 이수가 필요합니다◆")

                        else :
                            print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

                    elif ans5=='x':
                        print("◆전체 교양에서 33학점 이상 이수가 필요합니다◆")

                    else :
                        print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

                elif ans4=='x':
                    print("◆균형교양 이수가 필요합니다◆")

                else :
                    print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

            elif ans3=='x':
                print("◆상명핵심역량교양 이수가 필요합니다◆")

            else :
                print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

        elif ans2=='x':
            print("◆기초교양 이수가 필요합니다◆")

        else :
            print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

    elif ans1=='x':
        print()
        print("◆해당 프로젝트를 종료합니다◆")

    else :
        print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

elif ans0== 'x':
    print()
    ans1=input("상명대학교 행정학부 졸업프로젝트를 시작할까요? : ")
    print()
    if ans1== 'o' :
        print()
        print()
        print()
        print("<교양 관련 질문 START>")
        print()
        ans2=input("기초교양(13학점)을 모두 이수하였는가? : ")
        print()
        if ans2=='o' :
            ans3=input("상명핵심역량교양(4학점 이상)을 모두 이수하였는가? : ")
            print()
            if ans3== 'o' :
                ans4=input("균형교양(9학점 이상)을 모두 이수하였는가? : ")
                print()
                if ans4== 'o':
                    ans5=input("일반교양 포함 전체 교양 총 33학점 이상을 이수하였는가? : ")
                    print()
                    if ans5== 'o':
                        print("***교양 관련 졸업 조건 모두 충족***")
                        print()
                        print()
                        print()
                        print("<전공 관련 질문 START>")
                        ans6=input("심화전공, 다전공, 부전공 중 하나의 조건에서 전공 학점을 모두 이수하였는가? : ")
                        print()
                        if ans6=='o':
                            ans7=input("졸업고사 자격을 충족하였는가? : ")
                            print()
                            if ans7=='o':
                                ans8=input("졸업고사에 응시하여 통과하였는가? : ")
                                print()
                                if ans8=='o':
                                    print("♥축하합니다. 졸업이 가능합니다♥")

                                elif ans8=='x':
                                    print("※ 아쉽지만 졸업고사에 통과해야합니다 ※")

                                else:
                                    print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

                            elif ans7=='x':
                                print("◆8학기 이상을 이수하고 졸업시험 7과목 중 5과목과 행정통계학을 수강해야 합니다◆")

                            else :
                                print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

                        elif ans6=='x':
                            print("◆전공 학점 추가 이수가 필요합니다◆")

                        else :
                            print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

                    elif ans5=='x':
                        print("◆전체 교양에서 33학점 이상 이수가 필요합니다◆")

                    else :
                        print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

                elif ans4=='x':
                    print("◆균형교양 이수가 필요합니다◆")

                else :
                    print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

            elif ans3=='x':
                print("◆상명핵심역량교양 이수가 필요합니다◆")

            else :
                print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

        elif ans2=='x':
            print("◆기초교양 이수가 필요합니다◆")

        else :
            print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

    elif ans1=='x':
        print()
        print("◆해당 프로젝트를 종료합니다◆")

    else :
        print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")

else :
    print()
    print("XX 잘못된 대답입니다. 프로젝트를 다시 실행해주세요 XX")
    
