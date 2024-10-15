
export default function Header() {
    return (
        <header style={headerStyle}>
            <nav style={navStyle}>
                <h1 style={titleStyle}>読書アプリケーション</h1>
                <ul style={listStyle}>
                    <a href="/" style={linkStyle}>ホーム</a>
                    <a href="/search" style={linkStyle}>検索</a>
                </ul>
            </nav>
            <hr style={lineStyle} />
        </header>
    );
}

// スタイルオブジェクト
const headerStyle = {
    padding: '10px 20px',
    backgroundColor: '#f5f5f5',
};

const navStyle = {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
};

const titleStyle = {
    margin: 0,
    fontSize: '1.5rem',
};

const listStyle = {
    display: 'flex',
    gap: '20px',
    listStyleType: 'none',
    margin: 0,
    padding: 0,
};

const listItemStyle = {
    margin: 0,
};

const linkStyle = {
    textDecoration: 'none',
    color: 'black',
    fontWeight: 'bold',
};

const lineStyle = {
    border: 'none',
    borderBottom: '2px solid #ccc',
    marginTop: '10px',
};