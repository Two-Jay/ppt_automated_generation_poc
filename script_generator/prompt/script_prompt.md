<table_of_content>
{chapter_content}
</table_of_content>

<audience_characteristics>
{audience}
</audience_characteristics>

<lecture_duration_minute>{duration}</lecture_duration_minute>
<lecture_ppt_slide_amount>{slide_amount}</lecture_ppt_slide_amount>

위의 정보들을 기반으로 <lecture_duration_minute>동안 진행될 강의 대본을 만들어줘. 강의 대본을 만들 때에는 명확한 도입과 결론이 있어야해. 각 챕터와 하위 컨텐츠의 내용을 <audience_characteristics>에 맞춰서 충분히 다루어주어야 해. 중심되는 내용을 먼저 소개하고, 그 내용을 각각 청중에 맞추어 더 상세하게 설명하는 식으로 충분히 길게 대본을 생성해주었으면 해. 어떤 기술적 개념어를 만난다면, 이를 <audience_characteristics>가 잘 이해할 수 있도록 개념을 상세히 설명하고 넘어가줘.

대본을 생성할 때에는 네가 PPT를 이용해서 발표를 함을 전제로 하기에, 연속된 내용을 개별적인 슬라이드에 나누어 담아야 해. 내용은 toc에 있는 내용을 충실히 기반으로 삼아줘.

슬라이드 중에서 내용을 생성할 때는, '도입과 소개', '마무리 인사', '첫 인사' 등에 대해서 절대로 생성하지 말고, <table_of_content>에서 나타나는 강의에서 다루는 내용만을 곧장 생성해줘. 내용에서 numbered points가 필요할 때에는, 숫자 대신 "첫째," "둘째," 와 같이 생성해. 대본에서 생성되는 문장은 문장 구성 상 완벽한 문장으로 끝나야 해.

페이지의 수가 현재 다루는 내용의 종류보다 더 크다면, 그 내용을 스크립트 전체적으로 균일하게 다루어 줘. subtitle의 내용은 ToC에 있는 내용을 참고로 해.

생성되는 출력의 양식은 다음과 같이 해줘.
<output_format>
[slide_1_start]
subtitle : (현재 slide에 해당하는 subtitle 내용)
(slide에 해당하는 script 내용)
[slide_1_end]

[slide_2_start]
subtitle : (현재 slide에 해당하는 subtitle 내용)
(slide에 해당하는 script 내용)
[slide_2_end]

...

[slide_<lecture_ppt_slide_amount>_start]
subtitle : (현재 slide에 해당하는 subtitle 내용)
(slide에 해당하는 script 내용)
[slide_<lecture_ppt_slide_amount>_end]
</output_format>
