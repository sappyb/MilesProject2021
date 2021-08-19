
boring_state_extrinsic_keywords = ['grades', 'tests', 'test', 'score']
boring_state_intrinsic_keywords = ['career', 'interesting', 'fascinating']

boring_state_relevance_keywords = ['relevant', 'applicable']
boring_state_self_efficacy_keywords = ['improve', 'better']


def checkboringstate(list_of_words, msg_flags):
    count_intrinsic = 0
    count_extrinsic = 0
    count_self_efficacy = 0
    count_relevance = 0

    weight_of_externsic_internsic = 2
    flag = -1
    if int(msg_flags) == 1:
        for i in boring_state_intrinsic_keywords:
            if i in list_of_words:
                count_intrinsic += 1
        for i in boring_state_extrinsic_keywords:
            if i in list_of_words:
                count_extrinsic += 1
        if (weight_of_externsic_internsic * count_extrinsic > count_intrinsic):
            flag = 0
        else:
            flag = 1
        if count_extrinsic == 0 and count_intrinsic == 0:
            flag = -1

    if int(msg_flags) == 2:
        for i in boring_state_self_efficacy_keywords:
            if i in list_of_words:
                count_self_efficacy += 1
        if count_self_efficacy >= 1:
            flag = 2
        if flag == -1:
            flag = 5
    if int(msg_flags) == 3:
        for i in boring_state_relevance_keywords:
            if i in list_of_words:
                count_relevance += 1
        if count_relevance >= 1:
            flag = 3
        if flag == -1:
            flag = 6
    return flag

def checkkeywords(list_of_words, state, msg_flags):
    if int(state) == 2:
        flag_boring = checkboringstate(list_of_words, msg_flags)
        return flag_boring   
    else:
        return -1
    

