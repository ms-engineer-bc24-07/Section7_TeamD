
export default function Footer() {
    return (
        <footer style={footerStyle}>
            <p>&copy; 2024 My App. All rights reserved.</p>
            <hr style={lineStyle} />
        </footer>
    );
}

//スタイル・オブジェクト

const footerStyle = {
    padding: '10px 20px',
    backgroundColor: '#f5f5f5',
};

const lineStyle = {
    border: 'none',
    borderBottom: '2px solid #ccc',
    marginTop: '10px',
};