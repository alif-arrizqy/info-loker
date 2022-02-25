import json


def test_create_job(client, normal_user_token_headers):
    data = {
            "title": "SDE",
            "company": "impaction",
            "company_url": "string.com",
            "location": "jakarta timur",
            "description": "python",
            "date_posted": "2022-02-24"
        }
    response = client.post("/jobs/create-job/", data=json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["company"] == "impaction"
    assert response.json()["description"] == "python"