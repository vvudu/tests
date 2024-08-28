import pytest
import requests


is_test = True


class TestYD:
    def setup_method(self):
        self.headers = {
            'Authorization': 'y0_AgAAAABURG5tAADLWwAAAAEPFzn4AAAW_ZGbTEFKGL4XL-l2k42cYnfCDg'
        }

    @pytest.mark.parametrize(
        'param,folder_name,status',
        (
                ['path', 'Image', 201],
                ['path', 'Image', 409],
                ['pat', 'Music', 400],
        )
    )
    def test_create_folder(self, param, folder_name, status):
        params = {
            param: folder_name
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        assert response.status_code == status