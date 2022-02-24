import json


def test_create_job(client):
    data = {
            "title": "SDE",
            "company": "impaction",
            "company_url": "string.com",
            "location": "jakarta timur",
            "description": "python",
            "date_posted": "2022-02-24"
        }
    response = client.post("/jobs/create-job/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "impaction"
    assert response.json()["description"] == "python"