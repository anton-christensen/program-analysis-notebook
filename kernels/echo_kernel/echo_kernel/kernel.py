from ipykernel.kernelbase import Kernel

class EchoKernel(Kernel):
    implementation = 'Echo'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "Echo kernel - as useful as a parrot"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            # stream_content = {'name': 'stdout', 'text': "<h1>html data</h1>"}
            display_data_content = {    
                'data': {
                    'text/html': "test: <br><h1>fest uden hest</h1>"
                },
                'metadata': {}
            }
            # self.send_response(self.iopub_socket, 'stream', stream_content)
            self.send_response(self.iopub_socket, 'display_data', display_data_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
