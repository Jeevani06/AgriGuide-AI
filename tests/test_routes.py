def test_login_page(client):
    assert client.get("/login").status_code == 200
def test_full_flow(client):
    client.post("/register", data={"name": "A", "email": "a@x.com", "password": "pw"})
    client.post("/login", data={"email": "a@x.com", "password": "pw"})
    r = client.post("/recommend", data=dict(N=80, P=45, K=40, temperature=25, humidity=82, ph=6.2, rainfall=230))
    assert b"Rice" in r.data
    r = client.post("/monitor", data=dict(crop="rice", soil_moisture=20, N=80, P=45, K=40, temperature=25, humidity=82, rainfall=230))
    assert b"risk" in r.data
    r = client.post("/yield", data=dict(crop="rice", rainfall=1200, fertilizer=150, pesticide=2))
    assert b"tons/ha" in r.data
    assert b"recommendation" in client.get("/history").data
