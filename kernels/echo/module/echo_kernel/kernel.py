from ipykernel.kernelbase import Kernel
import os

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
    banner = "The echo kernel, by Anton"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            if code == "restart":
                self.send_response(self.iopub_socket, 'display_data', {    
                    'data': {
                        'text/html': "<script>Jupyter.notebook.kernel.restart()</script>"
                    },
                    'metadata': {}
                })
                

            #stream_content = {'name': 'stdout', 'text': "<h1>html data</h1>"}
            display_data_content = {    
                'data': {
                    'text/plain': 'this is simply text',
                    'text/html': "test: <h1>INGEN FEST</h1>"
                },
                'metadata': {}
            }
            #self.send_response(self.iopub_socket, 'stream', stream_content)
            self.send_response(self.iopub_socket, 'display_data', display_data_content)

        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
