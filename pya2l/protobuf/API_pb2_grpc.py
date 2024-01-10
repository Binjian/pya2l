# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobuf import API_pb2 as protobuf_dot_API__pb2


class A2LStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTreeFromA2L = channel.unary_unary(
                '/A2L/GetTreeFromA2L',
                request_serializer=protobuf_dot_API__pb2.TreeFromA2LRequest.SerializeToString,
                response_deserializer=protobuf_dot_API__pb2.TreeResponse.FromString,
                )
        self.GetJSONFromTree = channel.unary_unary(
                '/A2L/GetJSONFromTree',
                request_serializer=protobuf_dot_API__pb2.JSONFromTreeRequest.SerializeToString,
                response_deserializer=protobuf_dot_API__pb2.JSONResponse.FromString,
                )
        self.GetTreeFromJSON = channel.unary_unary(
                '/A2L/GetTreeFromJSON',
                request_serializer=protobuf_dot_API__pb2.TreeFromJSONRequest.SerializeToString,
                response_deserializer=protobuf_dot_API__pb2.TreeResponse.FromString,
                )
        self.GetA2LFromTree = channel.unary_unary(
                '/A2L/GetA2LFromTree',
                request_serializer=protobuf_dot_API__pb2.A2LFromTreeRequest.SerializeToString,
                response_deserializer=protobuf_dot_API__pb2.A2LResponse.FromString,
                )


class A2LServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTreeFromA2L(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJSONFromTree(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTreeFromJSON(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetA2LFromTree(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_A2LServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTreeFromA2L': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTreeFromA2L,
                    request_deserializer=protobuf_dot_API__pb2.TreeFromA2LRequest.FromString,
                    response_serializer=protobuf_dot_API__pb2.TreeResponse.SerializeToString,
            ),
            'GetJSONFromTree': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJSONFromTree,
                    request_deserializer=protobuf_dot_API__pb2.JSONFromTreeRequest.FromString,
                    response_serializer=protobuf_dot_API__pb2.JSONResponse.SerializeToString,
            ),
            'GetTreeFromJSON': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTreeFromJSON,
                    request_deserializer=protobuf_dot_API__pb2.TreeFromJSONRequest.FromString,
                    response_serializer=protobuf_dot_API__pb2.TreeResponse.SerializeToString,
            ),
            'GetA2LFromTree': grpc.unary_unary_rpc_method_handler(
                    servicer.GetA2LFromTree,
                    request_deserializer=protobuf_dot_API__pb2.A2LFromTreeRequest.FromString,
                    response_serializer=protobuf_dot_API__pb2.A2LResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'A2L', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class A2L(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTreeFromA2L(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/A2L/GetTreeFromA2L',
            protobuf_dot_API__pb2.TreeFromA2LRequest.SerializeToString,
            protobuf_dot_API__pb2.TreeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJSONFromTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/A2L/GetJSONFromTree',
            protobuf_dot_API__pb2.JSONFromTreeRequest.SerializeToString,
            protobuf_dot_API__pb2.JSONResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTreeFromJSON(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/A2L/GetTreeFromJSON',
            protobuf_dot_API__pb2.TreeFromJSONRequest.SerializeToString,
            protobuf_dot_API__pb2.TreeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetA2LFromTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/A2L/GetA2LFromTree',
            protobuf_dot_API__pb2.A2LFromTreeRequest.SerializeToString,
            protobuf_dot_API__pb2.A2LResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)