using Amazon.CDK;

namespace AwsCdkDotnet
{
    sealed class Program
    {
        public static void Main(string[] args)
        {
            var app = new App();
            var stackProps = new StackProps
            {
                Env = new Environment
                {
                    Region = "eu-west-1"
                }
            };
            new AwsCdkDotnetStack(app, "AwsCdkDotnetStack", stackProps);

            app.Synth();
        }
    }
}
