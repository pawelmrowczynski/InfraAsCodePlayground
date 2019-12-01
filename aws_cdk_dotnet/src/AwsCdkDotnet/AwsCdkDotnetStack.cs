using Amazon.CDK;
using Amazon.CDK.AWS.Lambda;

namespace AwsCdkDotnet
{
    public class AwsCdkDotnetStack : Stack
    {
        internal AwsCdkDotnetStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var hello = new Function(this, "JsHelloFromDotNetCdk", new FunctionProps
            {
                Runtime = Runtime.NODEJS_10_X, // execution environment
                Code = Code.FromAsset("lambda"), // Code loaded from the "lambda" directory
                Handler = "lambda.handler" // file is "hello", function is "handler"
            });
        }
    }
}
