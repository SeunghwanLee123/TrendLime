/* [검색 페이지] 검색 카테고리를 불러오는 키 */
export const fetchCategoryKey = `${process.env.REACT_APP_DB_HOST}/api/tags`;
/* [검색 페이지] 검색 카테고리 선택 시, 결과를 불러오는 키*/
export const fetchSearchKey = `${process.env.REACT_APP_DB_HOST}/api/search`;
/* [검색 페이지] 자동 완성 검색을 위한 샘플 검색 데이터를 불러오는 키*/
export const fetchAutoCompleteSearchKey = `${process.env.REACT_APP_DB_HOST}/api/search/total3/`;
/* [검색 페이지] 검색창에 입력된 인풋을 바탕으로 전체 검색 결과를 불러오는 키*/
export const featchTotalSearchKey = `${process.env.REACT_APP_DB_HOST}/api/search/total`;
/* [노래 페이지] 노래 기본 정보를 불러오는 키*/
export const featchSongInfoKey = `${process.env.REACT_APP_DB_HOST}/api/song/`;
/* [노래 페이지] 노래 가사 감정 정보를 불러오는 키*/
export const featchSongEmotionKey = `${process.env.REACT_APP_DB_HOST}/api/emotion/`;
/* [노래 페이지] 노래 가사 바탕 추천 결과를 보여주는 키*/
export const featchRecommendSongKey = `${process.env.REACT_APP_DB_HOST}/api/recommend/`;
/* [노래 페이지] 노래 토픽 데이터를 보여주는 키 */
export const featchSongTopicKey = `${process.env.REACT_APP_DB_HOST}/api/topic/`;
