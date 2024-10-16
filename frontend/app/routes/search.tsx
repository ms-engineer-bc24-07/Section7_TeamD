import { useState } from "react"; // useStateをインポート
import { Form } from "@remix-run/react";

export default function SearchPage() {
    const [books, setBooks] = useState([]); // 書籍を格納するための状態
    const [query, setQuery] = useState(""); // 現在のクエリを格納するための状態
    const [hasSearched, setHasSearched] = useState(false); // 検索が行われたかどうかの状態

    const handleSearch = async (event) => {
        event.preventDefault(); // デフォルトのフォーム送信を防ぐ

        // Google Books APIからデータを取得
        try {
            const response = await fetch(`https://www.googleapis.com/books/v1/volumes?q=${query}`);
            const data = await response.json();
            setBooks(data.items || []); // 取得した書籍を状態に設定
            setHasSearched(true); // 検索を行ったことを記録
        } catch (error) {
            console.error("Error fetching data:", error);
            setBooks([]); // エラー時は空の配列を設定
            setHasSearched(true); // 検索を行ったことを記録
        }
    };

    return (
        <div className="text-center mt-16">
            <h1>検索ワードを入力</h1>
            <Form onSubmit={handleSearch}>
                <input
                    type="text"
                    placeholder="あいまい検索：書名"
                    required
                    value={query} // 入力値をquery状態にバインド
                    onChange={(e) => setQuery(e.target.value)} // 変更時にquery状態を更新
                />
                <button type="submit" className="mt-4 p-2 text-lg bg-blue-500 text-white rounded">Search</button>
            </Form>

            {/* 検索結果を表示 */}
            <div className="mt-8">
                {hasSearched && books.length > 0 ? ( // 検索が行われたか確認
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        {books.map((book) => (
                            <div key={book.id} className="border p-4">
                                <h2 className="text-lg">{book.volumeInfo.title}</h2>
                                <img
                                    src={book.volumeInfo.imageLinks?.thumbnail}
                                    alt={book.volumeInfo.title}
                                    className="mt-2"
                                />
                                <p>{book.volumeInfo.authors?.join(", ")}</p>
                            </div>
                        ))}
                    </div>
                ) : hasSearched ? ( // 検索が行われたが、結果がない場合
                    <p>お探しの書籍が見つかりませんでした。</p>
                ) : null} {/* 検索が行われていない場合は何も表示しない */}
            </div>
        </div>
    );
}
