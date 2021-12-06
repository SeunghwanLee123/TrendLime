import React, { useMemo } from 'react';
import { useQuery } from 'react-query';
import { featchSongEmotionKey } from '../../utils/api/queryKeys';
import { useQueryFetch } from '../../utils/hooks/useQueryFetch';

import emotionMap from './emotionMap';

function EmotionSection({ songId }) {
    const { isLoading, error, data } = useQuery(
        [featchSongEmotionKey, { song_id: songId }],
        useQueryFetch,
        {
            initialData: [],
            refetchOnWindowFocus: false,
            refetchOnmount: false,
            refetchOnReconnect: false,
            retry: false,
        },
    );

    const { emotion, percentage } = useMemo(
        () => (data.emotion ? data.emotion : { emotion: '', percentage: '' }),
        [data],
    );

    const { emoji, word } = useMemo(
        () =>
            emotion === ''
                ? { emoji: '', word: '' }
                : { emoji: emotionMap[emotion].emoji, word: emotionMap[emotion].word },
        [emotion],
    );

    return (
        <div>
            <h3>가사의 주요 감정</h3>
            <div>
                {isLoading ? (
                    <p>감정 정보를 불러오고 있어요</p>
                ) : (
                    <p>
                        해당 곡은 <span>{emoji}</span>
                        {emotion}
                        {word} {percentage}% 가까워요!
                    </p>
                )}
            </div>
        </div>
    );
}

export default React.memo(EmotionSection);
