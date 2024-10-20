import { useState } from "react"; // useStateをインポート
import { Form } from "@remix-run/react";

// 追加：Bookの型を定義
interface Book {
    title: string;
    authors: string[];
    cover_image: string;
    isbn: string;
    published_date: string;
    description: string;
    page_count: number;
    categories: string[];
}

export default function SearchPage() {
    const [books, setBooks] = useState<Book[]>([]); // 変更：booksの型を指定
    const [query, setQuery] = useState(""); // 現在のクエリを格納するための状態
    const [hasSearched, setHasSearched] = useState(false); // 検索が行われたかどうかの状態
    // 変更：eventの型を指定
    const handleSearch = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault(); // デフォルトのフォーム送信を防ぐ

        // Google Books APIからデータを取得
        try {
            //変更：書籍検索エンドポイント（/search-books/）にリクエストを送る
            const response = await fetch(`${import.meta.env.VITE_API_URL}/search-books/?query=${query}`);
            const data = await response.json();
            console.log(data); //追加：返されたデータをコンソールに出力
            // 変更：取得した書籍を状態に設定(data.items→dataに変更)
            setBooks(data || []); 
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
                            <div key={book.isbn} className="border p-4"> {/* 変更：id→isbn */}
                                <h2 className="text-lg">{book.title}</h2> {/* 変更：book.volumeInfo.title→book.title */}
                                <img
                                //変更：book.volumeInfo.imageLinks?.thumbnail→book.cover_image
                                    src={book.cover_image} 
                                    alt={book.title}
                                    className="mt-2"
                                />
                                <p>{book.authors?.join(", ")}</p> {/* 変更：book.volumeInfo.authors?.join(", ") →book.authors.join(", ")  */}
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
