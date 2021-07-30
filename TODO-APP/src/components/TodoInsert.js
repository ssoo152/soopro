import React, { useState, useCallback } from 'react';
import { MdPlaylistAdd } from 'react-icons/md';
import './TodoInsert.scss';

const TodoInsert = ({onInsert}) => {
    const [value, setValue] = useState('');

    const onChange = useCallback(e => {
        setValue(e.target.value);
    }, []);

    const onSubmit = useCallback(
        e => {
            onInsert(value);
            setValue('');
            e.preventDefault();
        },
        [onInsert, value],
    );

    return (
        <form className="TodoInsert" onSubmit={onSubmit}>
            <input 
            placeholder="해야할 일 입력하기"
            value={value}
            onChange={onChange}
            />
            <button type="submit">
                < MdPlaylistAdd />
            </button>
        </form>

    );
};

export default TodoInsert;


