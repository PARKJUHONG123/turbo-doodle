{\rtf1\ansi\ansicpg949\cocoartf2511
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #include <string>\
#include <vector>\
\
using namespace std;\
\
vector<int> solution(vector<int> prices) \{\
    vector<int> answer;\
    int count = 0;\
    for (int i = 0; i < prices.size(); i++)\{\
        for (int j = i + 1; j < prices.size(); j++)\{\
            if (prices[i] <= prices[j])\{\
                count++;\
            \}\
            else\{\
                count++;\
                break;\
            \}\
        \}\
        answer.push_back(count);\
        count = 0;\
    \}\
    return answer;\
\}}