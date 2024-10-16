import { useEffect, useState } from "react";
import Header from "./layout_all/header";
import Footer from "./layout_all/footer";
import { Outlet } from "@remix-run/react";
import axios from "axios";

// 書籍データの型定義（オプション）
interface Book {
    id: string;
    volumeInfo: {
        title: string;
        imageLinks?: {
            thumbnail: string;
        };
    };
}

export default function Index() {
    const [books, setBooks] = useState<Book[]>([]);

    useEffect(() => {
        const fetchBooks = async () => {
            try {
                const response = await axios.get(
                    'https://www.googleapis.com/books/v1/volumes?q=${query}'
                );
                setBooks(response.data.items);
            } catch (error) {
                console.error("Failed to fetch books", error);
            }
        };
        fetchBooks();
    }, []);

    return (
        <div>
            <Header />
            <div style={bookContainerStyle}>
                {books.map((book) => (
                    <div key={book.id} style={bookStyle}>
                        <img
                            src={book.volumeInfo.imageLinks?.thumbnail}
                            alt={book.volumeInfo.title}
                            style={imageStyle}
                        />
                        <p>{book.volumeInfo.title}</p>
                    </div>
                ))}
            </div>
            <Outlet />
            <Footer />
        </div>
    );
}

const bookContainerStyle: React.CSSProperties = {
    display: "flex",
    flexWrap: "wrap",
    gap: "16px",
    padding: "16px",
    justifyContent: "center",
};

const bookStyle: React.CSSProperties = {
    width: "150px",
    padding: "10px",
    border: "1px solid #ddd",
    borderRadius: "8px",
    backgroundColor: "#f0f0f0",
    textAlign: "center",
};

const imageStyle: React.CSSProperties = {
    width: "100%",
    height: "200px",
    objectFit: "cover",
};
