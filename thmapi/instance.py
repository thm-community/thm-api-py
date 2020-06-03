from .util import *


class __THMInstance(object):
    def instance_running_instances(self) -> list:
        """
        AUTHENTICATED
        Gets the list of running instances

        :return: List of running instances
        """
        if not self.authenticated:
            raise Exception("Not authenticated")

        return http_get(self.session, '/api/running-instances')

    def instance_deploy(self, room_code, vm_id) -> dict:
        """
        AUTHENTICATED
        Deploys the selected VM in the room

        :param room_code: Room code to renew the VM in
        :param vm_id: VM id
        """
        if not self.authenticated:
            raise Exception("Not authenticated")

        csrf_token = fetch_pattern(self.session, f'/room/{room_code}', 'csrf-script')

        return http_post(
            self.session,
            '/deploy',
            data={'roomCode': room_code, 'id': vm_id},
            headers={'csrf-token': csrf_token},
            has_success=True
        )

    def instance_renew(self, room_code) -> float:
        """
        AUTHENTICATED
        Renews the VM in the selected room

        :param room_code: Room code to renew the VM in
        """
        if not self.authenticated:
            raise Exception("Not authenticated")

        csrf_token = fetch_pattern(self.session, f'/room/{room_code}', 'csrf-script')

        return http_post(
            self.session,
            '/api/vm/renew',
            data={'code': room_code},
            headers={'csrf-token': csrf_token},
            has_success=True
        )['timeInSeconds']

    def instance_terminate(self, room_code):
        """
        AUTHENTICATED
        Terminates the VM in the selected room

        :param room_code: Room code to terminate the VM in
        """
        if not self.authenticated:
            raise Exception("Not authenticated")

        csrf_token = fetch_pattern(self.session, f'/room/{room_code}', 'csrf-script')

        return http_post(
            self.session,
            '/api/vm/terminate',
            data={'code': room_code},
            headers={'csrf-token': csrf_token},
            has_success=True
        )
